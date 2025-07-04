import os
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS

os.environ["GOOGLE_API_KEY"] = st.secrets["GEMINI_API_KEY"]

def save_faiss_index(db, index_path="faiss_index.index"):
    """Simpan FAISS index ke disk."""
    db.save_local(index_path)

def load_faiss_index(index_path="faiss_index.index", embeddings=None):
    """Memuat FAISS index dari disk jika ada."""
    if os.path.exists(index_path):
        db = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
        return db
    return None

@st.cache_resource
def setup_rag_system(data_path="data/data.txt"):
    """
    Memuat data, membuat embeddings, dan menginisialisasi sistem RAG.
    """
    loader = TextLoader(data_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    db = load_faiss_index(embeddings=embeddings)
    if db is None:
        db = FAISS.from_documents(texts, embeddings)
        save_faiss_index(db) 
 
    retriever = db.as_retriever()

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def show():
    qa_chain = setup_rag_system()

    # Inject custom CSS for styling
    st.markdown("""
        <style>
        .main-title {
            text-align: center;
            font-size: 2.2em;
            color: #4F8BF9;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.1em;
            color: #666;
            margin-bottom: 2rem;
        }
        .chat-bubble {
            padding: 0.8rem 1.2rem;
            border-radius: 1rem;
            margin-bottom: 1rem;
        }
        .user-bubble {
            background-color: #e7f3ff;
            align-self: flex-end;
        }
        .assistant-bubble {
            background-color: #f2f2f2;
            align-self: flex-start;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown("<div class='main-title'>Chatbot Assistant</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Curious About Me? Just Ask!</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('assets/cat.jpg', width=350)
    # Initialize message state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat input
    if query := st.chat_input("Need help understanding my portfolio or just curious about my background? Ask away!"):
        st.session_state.messages.append({"role": "user", "content": query})

        with st.chat_message("user"):
            st.markdown(f"<div class='chat-bubble user-bubble'>{query}</div>", unsafe_allow_html=True)

        with st.chat_message("assistant"):
            with st.spinner("Loading..."):
                try:
                    result = qa_chain.invoke({"query": query})
                    response = result['result']
                    st.markdown(f"<div class='chat-bubble assistant-bubble'>{response}</div>", unsafe_allow_html=True)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_message = f"Error: {e}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": f"Error: {error_message}"})

                    