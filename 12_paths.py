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
    def __init__(value):
        self.value = value
        self.edges = list()
    
    def add_edge(self, vertex):
        self.edges.append(vertex)

    def get_edges(self):
        return self.edges
    
class Graph: 
    def __init__(self):
        self.graph = dict()
    
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex
    
    def add_edge(self, from_vertex, to_vertex):
        self.graph_dict[from_vertex.value].add_edge(to_vertex)
        self.graph_dict[to_vertex.value].add_edge(from_vertex)
    
    # find all paths method
    
    def find_all_paths(self):
        pass


# import input data into graph

caves = list()
connections = dict()

for entry in import_input_data:
    for cave in entry:
        if cave not in caves:
            caves.append(cave)
    if entry[0] not in connections:
        connections[entry[0]] = [entry[1]]
    else:
        if entry[1] not in connections[entry[0]]:
                connections[entry[0]].append(entry[1])
            
print()
print(caves)
print(connections)

# implement algorithm to find all paths from start to end



