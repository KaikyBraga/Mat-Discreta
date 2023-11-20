import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 
    
st.title("Graph's Training")

st.subheader("Praticidade")
st.write("Bem-vindo ao site Graph's Training! Esse é o aplicativo perfeito para validar o seu treino!")

st.subheader("Periodização de Treino")
st.write("Com o Graph's Training você consegue montar o seu treino na semana de maneira adequada e ainda consegue exibi-lo por meio de um grafo na tela!")

st.subheader("Seleção de Exercícios")
st.write("Aqui, você também pode fazer uma seleção de exercícios por grupamento muscular e verificar se a quantidade informada está condizente. A ferramenta também exibe de maneira gráfica a seleção do usuário.")

st.subheader("Aproveite ao máximo o aplicativo! 😁")
