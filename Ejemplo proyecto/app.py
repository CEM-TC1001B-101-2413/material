import streamlit as st

pages = [
    st.Page("page/home.py", title="Página de inicio"),
    st.Page("page/map.py", title="Ejemplo mapa"),
    st.Page("page/formulario.py", title="Formulario"),
    st.Page("page/IA.py", title="Uso de IA")
    ]

pg = st.navigation(pages)

pg.run()