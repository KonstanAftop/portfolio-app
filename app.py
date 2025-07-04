import streamlit as st
from streamlit_option_menu import option_menu
from sections import about, projects, chatbot  # Import chatbot.py

st.set_page_config(page_title="Konstan's Portfolio", layout="wide")

# Daftar halaman
menu_options = ["About Me", "Projects", "Chatbot"]

# Gunakan session_state untuk menyimpan halaman aktif
if "current_page" not in st.session_state:
    st.session_state.current_page = "About Me"

# Tentukan default_index
default_index = menu_options.index(st.session_state.current_page)

# Tampilkan menu NAVIGASI UTAMA
selected = option_menu(
    menu_title=None,
    options=menu_options,
    icons=["person", "folder2", "robot"],
    menu_icon="cast",
    default_index=default_index,
    orientation="horizontal",
    key="main_menu"
)

# Simpan pilihan menu ke session_state
if selected != st.session_state.current_page:
    st.session_state.current_page = selected

# GUNAKAN placeholder agar UI tidak hilang saat chat_input trigger reload
main_area = st.container()

with main_area:
    if st.session_state.current_page == "About Me":
        about.show()
    elif st.session_state.current_page == "Projects":
        projects.show()
    elif st.session_state.current_page == "Chatbot":
        chatbot.show()
