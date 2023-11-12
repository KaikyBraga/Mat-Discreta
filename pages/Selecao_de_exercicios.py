import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

with st.container():
    musculos_subcategorias = {
        'Nenhum': ['Nenhum'],
        'Braços': ['Bíceps', 'Tríceps', 'Antebraço'],
        'Pernas': ['Quadríceps', 'Posterior de coxa', 'Panturrilhas', 'Glúteos'],
        'Costas': ['Romboides', 'Deltoides', 'Trapézio', 'Dorsal'],
        'Core': ['Abdominais', 'Oblíquos', 'Lombar']
    }

    exercicios_subcategorias = {
        'Bíceps': ['Rosca Direta', 'Martelo', 'Bíceps corda', 'Rosca scott', 'Curls com barra', 'Curls com halteres'],
        'Tríceps': ['Tríceps na Polia', 'Rosca francesa', 'Tríceps Coice', 'Tríceps corda', 'Tríceps banco', 'Rosca testa'],
        'Antebraço': ['Rosca de punho', 'Rosca punho invertido', 'Rosca martelo', 'Flexão de dedos', 'Carregamento de halteres'],
        'Quadríceps': ['Agachamento', 'Agachamento Frontal', 'Leg Press', 'Cadeira Extensora', 'Afundo', 'Passada'],
        'Posterior de coxa': ['Stiff unilateral', 'Flexão de Pernas', 'Stiff', 'Cadeira Flexora', 'Cadeira Abdutora', 'Levantamento Terra'],
        'Panturrilhas': ['Elevação de Calcanhar em Pé', 'Elevação de Calcanhar Sentado', 'Pular Corda', 'Panturrilha no Smith', 'Panturrilha no Leg'],
        'Glúteos': ['Agachamento', 'Agachamento sumô', 'Afundo', 'Elevação pélvica', 'Extensão de quadril', 'Elevação unilateral'],
        'Romboides': ['Remada', 'Elevações Y Pronadas', 'Retração das Escápulas', 'Encolhimento de Ombros', 'Face Pulls'],
        'Deltoides': ['Face Pulls', 'Elevação Lateral', 'Posterior com Halteres', 'Remada Curvada', 'Remada Invertida', 'Elevações na Polia'],
        'Trapézio': ['Remada Alta', 'Remada com Halteres', 'Remada com Barra', 'Face Pulls'],
        'Dorsal': ['Barra Fixa', 'Puxada na Polia', 'Remada com Barra', 'Face Pulls', 'Levantamento Terra', 'Remada Curvada'],
        'Lombar': ['Hiperextensão Lombar', 'Remada Baixa', 'Prancha', 'Levantamento Terra'],
        'Abdominais': ['Crunch', 'Prancha Frontal', 'Elevação de Pernas', 'Torção Russa', 'Prancha Lateral', 'Abdominais Inferiores'],
        'Oblíquos': ['Torção Russa', 'Prancha Lateral', 'Elevação de Perna Lateral', 'Flexões Laterais']
    }

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Restrições de quantidade de exercícios por grupo muscular
    restricoes = {
        'Bíceps': (3, 5),
        'Tríceps': (3, 5),
        'Anti-braço': (2, 4),
        'Quadríceps': (3, 5),
        'Posterior de coxa': (3, 5),
        'Panturrilhas': (2, 4),
        'Glúteos': (3,5),
        'Romboides': (2, 4),
        'Deltoides': (3, 5),
        'Trapézio': (2,4),
        'Dorsal': (3, 5),
        'Lombar': (2, 3),
        'Abdominais': (2, 4),
        'Oblíquos': (2, 3),
    }

    def criar_subgrafo(grupo_muscular, musculo, exercicios):
        grafo = nx.DiGraph()

        grafo.add_node(grupo_muscular)
        grafo.add_node(musculo)
        grafo.add_edge(grupo_muscular, musculo)

        for exercicio in exercicios:
            grafo.add_node(exercicio)
            grafo.add_edge(musculo, exercicio)

        return grafo

    def verificar_restricoes(musculo, quantidade_selecionada):
        restricoes_musculo = restricoes.get(musculo)

        if restricoes_musculo is not None:
            min_restricao, max_restricao = restricoes_musculo
            if not min_restricao <= quantidade_selecionada <= max_restricao:
                st.error(f"CUIDADO! É recomendado selecionar de {min_restricao} a {max_restricao} exercícios para {musculo}.")

    def exibir_grafo(grafo):
        pos = nx.spring_layout(grafo)
        nx.draw(grafo, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=7, font_color="black", font_weight="bold", width=2, edge_color="gray")
        plt.title("Seleção de Grupo Muscular, Músculo e Exercício")
        st.pyplot()

    
    st.title("Selecione seus exercícios!")

    grupo_muscular = st.selectbox("Selecione o Grupo Muscular", list(musculos_subcategorias.keys()))

    if grupo_muscular != 'Nenhum':
        musculo = st.selectbox("Selecione o Músculo", musculos_subcategorias[grupo_muscular])
        exercicios_selecionados = st.multiselect("Selecione os Exercícios", exercicios_subcategorias[musculo])

        verificar_restricoes(musculo, len(exercicios_selecionados))

        subgrafo = criar_subgrafo(grupo_muscular, musculo, exercicios_selecionados)
        exibir_grafo(subgrafo)

        st.write("Grupo Muscular Selecionado:", grupo_muscular)
        st.write("Músculo Selecionado:", musculo)
        st.write("Exercícios Selecionados:", exercicios_selecionados)

    