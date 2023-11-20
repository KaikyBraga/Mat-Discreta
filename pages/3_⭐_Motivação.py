import streamlit as st
from PIL import Image, ImageDraw, ImageOps

st.set_page_config(page_title="Motivação")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

    st.title("Motivação")

    # Carregar as imagens
    kaiky = Image.open("imagens/kaiky.jpg")
    samuel = Image.open("imagens/samuel.jpg")

    # Tamanho desejado para as imagens redondas
    tamanho_redondo = (2000, 2000)

    # Criar máscaras circulares
    def aplicar_mascara(imagem, mascara):
        imagem = ImageOps.fit(imagem, mascara.size, centering=(0.5, 0.5))
        imagem.putalpha(mascara)
        return imagem

    mascara = Image.new("L", tamanho_redondo, 0)
    draw = ImageDraw.Draw(mascara)
    draw.ellipse((0, 0) + tamanho_redondo, fill=255)

    kaiky = aplicar_mascara(kaiky, mascara)
    samuel = aplicar_mascara(samuel, mascara)

    # Adicionar margens transparentes às imagens para criar espaço entre elas
    kaiky = ImageOps.expand(kaiky, border=30, fill=None)
    samuel = ImageOps.expand(samuel, border=30, fill=None)

    # Exibir imagens redondas lado a lado com espaçamento e nomes abaixo delas
    st.image([kaiky, samuel], width=230, caption=["Kaiky Braga", "Samuel Lima"])

    st.write("Olá! Somos alunos do 2° Período de Ciência de Dados da Escola de Matemática Aplicada da Fundação Getúlio Vargas, iniciamos este projeto com o intuito de representar por meio de Grafos estruturas de treinos de musculação válidas. Tudo isso somado com a interatividade proporcionada pela biblioteca Streamlit.")

with st.container():
    if st.button("Clique para acessar o projeto no GitHub :)"):
        site_url = "https://github.com/KaikyBraga/Mat-Discreta"
        st.write(f'<meta http-equiv="refresh" content="0; url={site_url}" />', unsafe_allow_html=True)
