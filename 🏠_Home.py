import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 
    
st.title("Graph's Training")

st.subheader("Eficiência Redefinida: Bem-vindo ao Graph's Training!")
st.write("Descubra a praticidade redefinida com o Graph's Training, o seu aplicativo ideal para otimizar e validar o seu treino!")

st.subheader("Periodização de Treino")
st.write("Com o Graph's Training, você tem o poder de estruturar sua semana de treino de maneira personalizada, visualizando-a de forma clara e intuitiva através de um grafo dinâmico na tela.")

st.subheader("Seleção de Exercícios")
st.write("Facilitamos a seleção de exercícios! Agora, você pode escolher seus exercícios por grupamento muscular, garantindo que a quantidade selecionada esteja perfeitamente alinhada com suas metas. Nossa ferramenta apresenta visualizações gráficas envolventes para acompanhar cada seleção.")

st.subheader("Aproveite ao máximo o aplicativo! 😁")
