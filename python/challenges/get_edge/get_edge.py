from graph import Graph, Vertex, Edge

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

    
cities = ['Portland', 'San Francisco', 'Portland']

def get_edges(graph, cities):

    ticket = 0
    vertices = []
    
    if len(cities) <= 1:
        return (False, 0)

    while len(cities) > 1:
        direct_flight = False

        # get all vertices from graph
        for vertex in graph.get_vertices():
            for city in cities:
                if city == vertex.value:
                    if vertex not in vertices:
                        vertices.append(vertex)
        
        start_city = cities[0]
        end_city = cities[1]
        city1_destinations = trip.get_neighbours(vertices[0])
    
        for destination in city1_destinations:
            if destination[0] == end_city:
                direct_flight = True
                ticket += destination[1]
        
        if not direct_flight:
            ticket = 0
        
        cities.remove(start_city)
        vertices.remove(vertices[0])
    
    return (direct_flight, ticket)
    
print(get_edges(trip, cities))