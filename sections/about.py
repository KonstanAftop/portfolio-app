import streamlit as st

def show():
    st.title("About Me")
    st.markdown("""
        <style>
        img {
            border-radius: 50%;
            height: 200px !important;
            width: 200px !important;
            object-fit: cover;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/nc.jpg")
    with col2:
        st.markdown("""
        <h3>Konstan Aftop</h3>
        <p><strong>Data Scientist / Machine Learning Engineer</strong><br>
        📍 Bandung, Indonesia<br>
        📧 konstanaftopds@gmail.com<br>
        🔗 <a href="https://www.linkedin.com/in/konstanaftop25/" target="_blank">LinkedIn</a></p>
        """, unsafe_allow_html=True)

    st.markdown("---")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 💼 Experiences")
        st.markdown("""
        - 🏢 **ML Engineer Cohort** – Coding Camp by DBS Foundation (Feb 2025– Jul 2025)  
          I developed individual projects such as data analysis dashboards using Streamlit, image classification models, and time-series forecasting by applying both machine learning and deep learning techniques. As a final project, I worked with machine learning, frontend, and backend teams to prepare production-ready models for deployment in SuaTalk, a baby cry detection and recommendation app, where I successfully improved the cry detection model’s accuracy to 91% through iterative experimentation and optimization.

        - 🏢 **Climate Data Analyst** – Meteorologi ITB X PLN (2025)  
          I contributed to a research project on future rainfall projections and their implications for hydropower potential at the Mrica Reservoir under the ITB-PLN partnership. My focus was on processing and analyzing Global Climate Model (GCM) outputs, performing ensemble analysis, and deriving rainfall trends and variability using Python libraries such as Pandas, Xarray, and Matplotlib. This work supported the analytical workflow used in a graduate thesis aimed at informing long-term energy sector planning.
        """)
    with col4:
        st.markdown("### 🧰 Skills")
        st.markdown("""
        - Python, scikit-learn, TensorFlow  
        - LangChain, Flask, Streamlit  
        - Git, Linux
        """)

    st.markdown("---")

    with open("assets/KonstanAftopAnewataNdruru_CV_Academy2026.pdf", "rb") as f:
        cv_bytes = f.read()

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        st.download_button(
            label="📄 Download CV",
            data=cv_bytes,
            file_name="cv_konstan.pdf",
            mime="application/pdf",
            use_container_width=True
        )
