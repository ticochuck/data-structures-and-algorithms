import pytest

from graph import Edge, Graph, Vertex


def test_Graph_exits():
    assert Graph


def test_Vertex_exits():
    assert Vertex


def test_Edge_exits():
    assert Edge


def test_create_graph():
    graph = Graph()
    assert graph


def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex('chuck')
    assert vertex.value == 'chuck'


def test_add_edge():
    graph = Graph()
    vertex1 = graph.add_vertex('ham')
    vertex2 = graph.add_vertex('eggs')
    graph.add_edge(vertex1, vertex2, 11)
    assert graph.adjacency_list[vertex1][0].vertex == vertex2


def test_add_edge_raises_error():
    graph = Graph()
    vertex1 = graph.add_vertex('ham')
    vertex2 = ''
    with pytest.raises(KeyError):
        assert graph.add_edge(vertex1, vertex2, 11)


def test_size_pass():
    graph = Graph()
    vertex1 = graph.add_vertex('ham')
    vertex2 = graph.add_vertex('eggs')
    graph.add_edge(vertex1, vertex2, 11)
    assert len(graph.adjacency_list) == 2 
    

def test_size_fail():
    graph = Graph()
    vertex1 = graph.add_vertex('ham')
    vertex2 = graph.add_vertex('eggs')
    graph.add_edge(vertex1, vertex2, 11)
    assert len(graph.adjacency_list) != 4 


def test_get_vertices():
    graph = Graph()
    vertex1 = graph.add_vertex('avocado')
    vertex2 = graph.add_vertex('cheese')
    graph.add_edge(vertex1, vertex2, 11)
    output = graph.get_vertices()
    assert output == ['avocado', 'cheese']


def test_get_vertices_multiple():
    trip = Graph()
    city1 = trip.add_vertex('Seattle')
    city2 = trip.add_vertex('Portland')
    city3 = trip.add_vertex('San Francisco')
    city4 = trip.add_vertex('Salt Lake City')
    city5 = trip.add_vertex('Spokane')
    trip.add_edge(city1, city2, 11)
    trip.add_edge(city2, city3, 12)
    trip.add_edge(city3, city4, 13)
    trip.add_edge(city4, city5, 14)
    trip.add_edge(city5, city1, 15)
    output = trip.get_vertices()
    assert output == ['Seattle', 'Portland', 'San Francisco', 'Salt Lake City', 'Spokane']



