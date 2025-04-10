def is_hamiltonian_path(graph, path):
    visited = set()
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        if v in visited or v not in graph[u]:
            return False
        visited.add(u)
    visited.add(path[-1])
    return len(visited) == len(graph)

def hamiltonian_util(graph, path, visited):
    if len(path) == len(graph):
        return True

    for vertex in graph:
        if vertex not in visited and (not path or vertex in graph[path[-1]]):
            visited.add(vertex)
            path.append(vertex)
            if hamiltonian_util(graph, path, visited):
                return True
            visited.remove(vertex)
            path.pop()
    return False

def find_hamiltonian_path(graph):
    for start in graph:
        path = [start]
        visited = {start}
        if hamiltonian_util(graph, path, visited):
            return path
    return None

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    path = find_hamiltonian_path(graph)
    if path:
        print("Caminho Hamiltoniano encontrado:", path)
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")
