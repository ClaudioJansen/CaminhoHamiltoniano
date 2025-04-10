import networkx as nx
import matplotlib.pyplot as plt

def draw_graph_with_path(graph, path=None):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1200, font_weight='bold')

    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    plt.title("Visualização do Grafo e Caminho Hamiltoniano")
    plt.savefig("assets/hamiltonian_path.png")
    plt.show()

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    from main import find_hamiltonian_path
    path = find_hamiltonian_path(graph)
    draw_graph_with_path(graph, path)
