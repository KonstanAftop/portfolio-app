import streamlit as st
import json
import math

def show():
    st.markdown("""
        <style>
        .element-container:has(img) img {
            height: 180px;
            object-fit: cover;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Load data proyek
    with open("data/projects.json") as f:
        projects = json.load(f)

    NUM_PER_PAGE = 3
    TOTAL = len(projects)
    TOTAL_PAGES = math.ceil(TOTAL / NUM_PER_PAGE)

    if "project_page" not in st.session_state:
        st.session_state.project_page = 0

    start_idx = st.session_state.project_page * NUM_PER_PAGE
    end_idx = start_idx + NUM_PER_PAGE
    visible_projects = projects[start_idx:end_idx]

    st.title("📁 Projects")

    cols = st.columns(3)
    for col, project in zip(cols, visible_projects):
        with col:
            with st.container():
                st.image(f"assets/{project['gambar']}", use_container_width=True)

                # Judul project
                st.markdown(f"### {project['nama']}")

                # Informasi tipe dan genre
                st.markdown(f"**{project['tipe']}** – {project['genre']}")

                # Deskripsi
                st.markdown(project['deskripsi'])

                # Tools
                st.markdown(f"<small><i>Tools: {', '.join(project['tools'])}</i></small>", unsafe_allow_html=True)

                # Tautan GitHub jika tersedia
                if "github" in project and project["github"]:
                    st.markdown(f"🔗[View on GitHub]({project['github']})")

    # Navigasi halaman
    col1, col2, col3 = st.columns([1, 1, 2])
    rerun_triggered = False

    with col1:
        if st.button("⬅️ Prev", key="prev_button") and st.session_state.project_page > 0:
            st.session_state.project_page -= 1
            rerun_triggered = True

    with col2:
        if st.button("Next ➡️", key="next_button") and st.session_state.project_page < TOTAL_PAGES - 1:
            st.session_state.project_page += 1
            rerun_triggered = True

    with col3:
        st.markdown(f"**Page {st.session_state.project_page + 1} of {TOTAL_PAGES}**")

    if rerun_triggered:
        st.rerun()
