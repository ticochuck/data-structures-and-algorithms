class Graph:
    
    def __init__(self):
        self.adjacency_list = {}


    def add_vertex(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    
    def add_edge(self, start_vertex, end_vertex, weight=1):
        
        # check if start and end vertices are in the adjency_list        
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError('Start or End Vertex not in the graph')
        
        
        edge = Edge(end_vertex, weight)
        adjacencies = self.adjacency_list[start_vertex]
        adjacencies.append(edge)

        
    def size(self):
        return len(self.adjacency_list)

    
    def get_vertices(self):
        """
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        """
        output = []
        
        for vertex in self.adjacency_list:
            output.append(vertex.value)

        return output

    def get_neighbours(self, vertex):
        """
        Returns a collection of edges connected to the given node
        Takes in a given node
        Include the weight of the connection in the returned collection
        """
        output = []
        
        if vertex in self.adjacency_list:
            # print(self.adjacency_list[vertex][1].vertex.value)
            for neighbour in self.adjacency_list[vertex]:
                output.append([neighbour.vertex.value, neighbour.weight])
                
        return output

    

class Vertex:
    """
    This is equivalent to a Node...
    """
    def __init__(self, value):
        self.value = value


class Edge:
    
    def __init__(self, end_vertex, weight=1):
        self.vertex = end_vertex
        self.weight = weight



