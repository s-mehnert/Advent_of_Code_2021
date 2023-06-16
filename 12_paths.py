#***** ADVENT OF CODE 2021 *****
#************ DAY 12 ***********
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("12_paths_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n").split("-"))

print(import_input_data)
print()
for line in import_input_data:
    print(line)


# create graph with caves as vertices and edges for the connections between them

class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = list()
    
    def add_edge(self, vertex):
        self.edges.append(vertex)

    def get_edges(self):
        return self.edges
    
class Graph: 
    def __init__(self):
        self.graph_dict = dict()
    
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex
    
    def add_edge(self, from_vertex, to_vertex):
        self.graph_dict[from_vertex.value].add_edge(to_vertex)
        self.graph_dict[to_vertex.value].add_edge(from_vertex)
    
    # find all paths method
    
    def find_all_paths(self, from_vertex, to_vertex):
        pass


# import input data into graph --> continue here

caves = list()

for entry in import_input_data:
    for cave in entry:
        if cave not in caves:
            caves.append(cave)

connections = {cave : [] for cave in caves}

for entry in import_input_data:
    connections[entry[0]].append(entry[1])
    connections[entry[1]].append(entry[0])

            
print()
print(caves)
print(connections)

cave_system = Graph()

for cave in caves:
    vertex = Vertex(cave)
    cave_system.add_vertex(vertex)

for cave in caves:
    vertex = Vertex(cave)
    cave_system.add_vertex(vertex)
    for key, value in connections.items():
        if key == cave:
            for connection in value:
                vertex.add_edge(connection)

print()
print(cave_system.graph_dict)
print()
for cave in cave_system.graph_dict:
    print("\nCave:", cave)
    for edge in cave_system.graph_dict[cave].edges:
        print("  --> ", edge)




# implement algorithm to find all paths from start to end



