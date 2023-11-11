import streamlit as st

st.set_page_config(page_title="Trabalho de Matemática Discreta")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

with st.container():
    st.title("Crie seu treino com grafos!")
    st.write("Quer acessar o projeto pelo GitHub? [Clique aqui](https://github.com/KaikyBraga/Mat-Discreta.git)")