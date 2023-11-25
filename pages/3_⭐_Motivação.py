import streamlit as st
from streamlit.components.v1 import html
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
    st.image([kaiky, samuel], width=350, caption=["Kaiky Braga", "Samuel Lima"])

    st.write("Olá! Nós, estudantes do 2º Período de Ciência de Dados da Escola de Matemática Aplicada da Fundação Getúlio Vargas, estamos entusiasmados em compartilhar nosso projeto, no qual buscamos visualizar de maneira gráfica as estruturas de treinos de musculação utilizando Grafos. Essa abordagem é aprimorada com a interatividade proporcionada pela biblioteca Streamlit. Estamos ansiosos para apresentar os resultados desta iniciativa que integra a precisão dos dados com a dinâmica da visualização, proporcionando uma experiência informativa e envolvente.")



# URL que você quer abrir
link = "https://github.com/KaikyBraga/Mat-Discreta"

# Criar o botão no Streamlit
if st.button("Acessar Link"):
    # Adicionar código HTML e JavaScript para abrir o link na mesma janela
    js_code = f"window.open('{link}', '_self');"
    html_code = f'<script>{js_code}</script>'
    html(html_code)