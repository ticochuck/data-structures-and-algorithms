from graph import Graph, Edge, Vertex
from get_edge import get_edges


def test_Graph():
    assert Graph


def test_valid_trip():
    trip = Graph()
    city1 = trip.add_vertex('Seattle')
    city2 = trip.add_vertex('Portland')
    city3 = trip.add_vertex('San Francisco')
    city4 = trip.add_vertex('Salt Lake City')
    city5 = trip.add_vertex('Spokane')
    city6 = trip.add_vertex('Los Angeles')
    trip.add_edge(city1, city2, 100)
    trip.add_edge(city2, city1, 110)
    trip.add_edge(city2, city3, 120)
    trip.add_edge(city3, city2, 130)
    trip.add_edge(city3, city4, 140)
    trip.add_edge(city4, city3, 150)
    trip.add_edge(city4, city5, 160)
    trip.add_edge(city5, city4, 170)
    trip.add_edge(city5, city6, 180)
    trip.add_edge(city6, city5, 190)
    trip.add_edge(city3, city5, 200)
    trip.add_edge(city5, city3, 210)
    trip.add_edge(city1, city6, 220)
    trip.add_edge(city6, city1, 230)
    cities = ['Seattle', 'Portland']
    actual = get_edges(trip, cities) 
    expected = (True, 100)
    assert actual == expected

destinations = ['Seattle', 'Portland', 'San Francisco']

def test_valid_trip_3_cities():
    trip = Graph()
    city1 = trip.add_vertex('Seattle')
    city2 = trip.add_vertex('Portland')
    city3 = trip.add_vertex('San Francisco')
    city4 = trip.add_vertex('Salt Lake City')
    city5 = trip.add_vertex('Spokane')
    city6 = trip.add_vertex('Los Angeles')
    trip.add_edge(city1, city2, 100)
    trip.add_edge(city2, city1, 110)
    trip.add_edge(city2, city3, 120)
    trip.add_edge(city3, city2, 130)
    trip.add_edge(city3, city4, 140)
    trip.add_edge(city4, city3, 150)
    trip.add_edge(city4, city5, 160)
    trip.add_edge(city5, city4, 170)
    trip.add_edge(city5, city6, 180)
    trip.add_edge(city6, city5, 190)
    trip.add_edge(city3, city5, 200)
    trip.add_edge(city5, city3, 210)
    trip.add_edge(city1, city6, 220)
    trip.add_edge(city6, city1, 230)
    actual = get_edges(trip, destinations) 
    expected = (True, 220)
    assert actual == expected