import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st


def criar_rotina_semanal(grupamentos):
    # Criando um grafo cíclico (um ciclo) representando os dias da semana
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    grafo = nx.cycle_graph(dias_semana)

    # Adicionando restrições com base nos grupamentos fornecidos
    for dia, grupamento in grupamentos.items():
        vizinhos = list(grafo.neighbors(dia))

        # Remover arestas para não treinar o mesmo grupamento em dias consecutivos
        if grupamento != "Descanso":
            for vizinho in vizinhos:
                if grupamento == grupamentos.get(vizinho, None):
                    grafo.remove_edge(dia, vizinho)

    return grafo

def is_cycle(grafo):
    try:
        nx.find_cycle(grafo)
        return True
    except nx.NetworkXNoCycle:
        return False


def colorir_grafo(grafo, grupamentos):
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
    nx.draw(grafo, pos, with_labels=True, font_weight="bold", node_size=700, node_color=cores, ax=ax)

    if "Treino" in grafo.graph and grafo.graph["Treino"] == "Inválido":
        plt.text(0.5, 0.5, "Treino Inválido (Grafo Acíclico)", fontsize=20, ha="center", va="center", color="red", transform=plt.gca().transAxes)
    else: 
        plt.text(0.5, 0.5, "Treino Válido (Grafo com Ciclo)", fontsize=20, ha="center", va="center", color="green", transform=plt.gca().transAxes)

    legenda = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=cor, markersize=10, label=grupo)
               for grupo, cor in cores_mapping.items()]
    plt.legend(handles=legenda, title="Grupos Musculares", loc="upper left")

    # Exibir a figura no Streamlit passando a figura como argumento
    st.pyplot(fig)

# Exemplo de grupamentos musculares
"""
grupamentos_exemplo = {
    "Segunda": "Pernas",
    "Terça": "Peito",
    "Quarta": "Costas",
    "Quinta": "Ombros",
    "Sexta": "Braços",
    "Sábado": "Descanso",
    "Domingo": "Descanso",
}
"""

# Criar e visualizar a rotina com base nos grupamentos de exemplo
#rotina = criar_rotina_semanal(grupamentos_exemplo)
#colorir_grafo(rotina, grupamentos_exemplo)