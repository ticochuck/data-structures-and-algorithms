from graph import Graph


visited = []

def depth_first_graph(visited, graph, vertex):
    

    if vertex not in visited:
        visited.append(vertex)

        for neighbour in graph[vertex]:
            depth_first_graph(visited, graph, neighbour)
    
    return visited


