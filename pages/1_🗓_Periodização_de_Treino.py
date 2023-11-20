import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


st.set_page_config(page_title="Trabalho de Matemática Discreta")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 

with st.container():
    # Dicionário inicial de exemplos de grupamentos para cada dia da semana
    grupamentos_exemplo = {
            "Segunda": "Descanso",
            "Terça": "Descanso",
            "Quarta": "Descanso",
            "Quinta": "Descanso",
            "Sexta": "Descanso",
            "Sábado": "Descanso",
            "Domingo": "Descanso",
        }
    
    st.title("Selecione as atividades para cada dia da semana")

    # Atividades Disponíveis
    atividades = ["Descanso", "Peito", "Costas", "Braços", "Ombros", "Pernas"]
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    segunda = col1.selectbox("Segunda", atividades)
    terca = col2.selectbox("Terça", atividades)
    quarta = col3.selectbox("Quarta", atividades)
    quinta = col4.selectbox("Quinta", atividades)
    sexta = col5.selectbox("Sexta", atividades)
    sabado = col6.selectbox("Sábado", atividades)
    domingo = col7.selectbox("Domingo", atividades)

    if st.button("Salvar Atividades"):
        # Dicionário para armazenar as atividades selecionadas
        grupamentos_exemplo = {
            "Segunda": segunda,
            "Terça": terca,
            "Quarta": quarta,
            "Quinta": quinta,
            "Sexta": sexta,
            "Sábado": sabado,
            "Domingo": domingo,
        }

    def criar_rotina_semanal(grupamentos):
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        # Criação de Grafo com Ciclo representando os dias da semana
        grafo = nx.cycle_graph(dias_semana)

        # Adicionando restrições com base nos grupamentos fornecidos
        for dia, grupamento in grupamentos.items():
            vizinhos = list(grafo.neighbors(dia))
            # Remoção de arestas para não existir mesma coloração adjacente
            if grupamento != "Descanso":
                for vizinho in vizinhos:
                    if grupamento == grupamentos.get(vizinho, None):
                        grafo.remove_edge(dia, vizinho)

        return grafo
    
    # Função para verificar se o grafo é cíclico
    def is_cycle(grafo):
        try:
            nx.find_cycle(grafo)
            return True
        except nx.NetworkXNoCycle:
            return False


    def colorir_grafo(grafo, grupamentos):
        """
        Função para colorir o grafo e exibi-lo visualmente
        """
        if not is_cycle(grafo):
            grafo.graph["Treino"] = "Inválido"

        cores_mapping = {
            "Pernas": "red",
            "Peito": "blue",
            "Costas": "green",
            "Ombros": "purple",
            "Braços": "orange",
            "Descanso": "lightgrey",
        }

        cores = [cores_mapping[grupamentos[dia]] for dia in grafo.nodes]
        pos = nx.circular_layout(grafo)

        fig, ax = plt.subplots()
        
        # Ajuste do tamanho da fonte dos textos nos vértices
        nx.draw(grafo, pos, with_labels=True, font_size=10, node_size=700, node_color=cores, ax=ax)

        if "Treino" in grafo.graph and grafo.graph["Treino"] == "Inválido":
            plt.text(0.5, 0.5, "Treino Inválido (Grafo Acíclico)", fontsize=13, ha="center", va="center", color="red", transform=plt.gca().transAxes)
        else: 
            plt.text(0.5, 0.5, "Treino Válido (Grafo com Ciclo)", fontsize=13, ha="center", va="center", color="green", transform=plt.gca().transAxes)

        legenda = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=cor, markersize=8, label=grupo)
                for grupo, cor in cores_mapping.items()]

        # Configurações de texto e da legenda
        plt.legend(handles=legenda, loc="upper left", fontsize=7)
        plt.title("Treino Semanal", fontsize=10, style="oblique", backgroundcolor="red", color="white",size="large")

        # Exibição do grafo no Streamlit
        st.pyplot(fig)

    rotina = criar_rotina_semanal(grupamentos_exemplo)
    colorir_grafo(rotina, grupamentos_exemplo)


        

        
    

