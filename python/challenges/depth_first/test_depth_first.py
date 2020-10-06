from graph import Edge, Graph, Vertex
from depth_first import depth_first_graph


def test_graph_exist():
    assert Graph


def test_depth_first():
    assert depth_first_graph




def test_deph_first():
    graph = {
        'A' : ['B'],
        'B' : ['D', 'C', 'E'],
        'C' : [],
        'D' : ['A'],
        'E' : [],
        }
    visited = []
    assert depth_first_graph(visited, graph, 'A') == ['A','B','D','C','E']