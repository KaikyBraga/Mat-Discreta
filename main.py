import networkx as nx
import matplotlib.pyplot as plt

def criar_rotina_semanal(grupamentos):
    # Criando um grafo cíclico (um ciclo) representando os dias da semana
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    grafo = nx.cycle_graph(dias_semana)

    # Adicionando a aresta para ligar o domingo à segunda-feira
    grafo.add_edge('Domingo', 'Segunda')

    # Adicionando restrições com base nos grupamentos fornecidos
    for dia, grupamento in grupamentos.items():
        vizinhos = list(grafo.neighbors(dia))

        # Remover arestas para não treinar o mesmo grupamento em dias consecutivos
        for vizinho in vizinhos:
            if grupamento == grupamentos.get(vizinho, None):
                grafo.remove_edge(dia, vizinho)

    return grafo

def colorir_grafo(grafo, grupamentos):
    # Mapear explicitamente os nomes dos grupos musculares para cores
    cores_mapping = {
        'Pernas': 'red',
        'Peito': 'blue',
        'Costas': 'green',
        'Ombros': 'purple',
        'Braços': 'orange',
        'Descanso': 'gray',
    }

    # Atribuir cores com base no mapeamento
    cores = [cores_mapping[grupamentos[dia]] for dia in grafo.nodes]

    # Criar um layout para a visualização do grafo
    pos = nx.circular_layout(grafo)

    # Desenhar o grafo colorindo os nós de acordo com os grupamentos
    nx.draw(grafo, pos, with_labels=True, font_weight='bold', node_size=700, node_color=cores)

    plt.show()

# Exemplo de grupamentos musculares
grupamentos_exemplo = {
    'Segunda': 'Pernas',
    'Terça': 'Peito',
    'Quarta': 'Costas',
    'Quinta': 'Ombros',
    'Sexta': 'Braços',
    'Sábado': 'Descanso',
    'Domingo': 'Descanso',
}

# Criar e visualizar a rotina com base nos grupamentos de exemplo
rotina = criar_rotina_semanal(grupamentos_exemplo)
colorir_grafo(rotina, grupamentos_exemplo)