#***** ADVENT OF CODE 2021 *****
#************ DAY 12 ***********
#****************** Part 1 *****


# get input data

import_input_data = list()

with open("12_paths_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(line.strip("\n").split("-"))

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
    
    # find all paths method --> fix this
    
    def find_all_paths(self, from_vertex, to_vertex):
        all_paths = list()
        path = [from_vertex]
        current_vertex = from_vertex
        next_caves = self.graph_dict[from_vertex].get_edges()

        while path:
            count = 0
            while next_caves:
                count += 1
                print("Current vertex:", current_vertex)
                print("Path:", path)
                print("Next caves:", next_caves)
                #print("Next caves:", next_caves)
                current_vertex = next_caves.pop()
                if current_vertex == from_vertex or current_vertex == path[-1]:
                    path.pop()
                    remove = True
                    for edge in self.graph_dict[path[-1]].get_edges():
                        if edge not in path:
                            remove = False
                    if remove:
                        path.pop()
                    continue

                if current_vertex in path:
                    if current_vertex.islower():
                        remove = True
                        for edge in self.graph_dict[path[-1]].get_edges():
                            if edge not in path:
                                remove = False
                        if remove:
                            path.pop()
                        continue
                
                path.append(current_vertex)

                if current_vertex == to_vertex:
                    all_paths.append([path[:]])
                    print("Found path:", path)
                    path.pop()
                    remove = True
                    for edge in self.graph_dict[path[-1]].get_edges():
                        if edge not in path:
                            remove = False
                    if remove:
                        path.pop()
                    continue

                append = False
                for edge in self.graph_dict[path[-1]].get_edges():
                    if edge not in path or edge.isupper():
                        append = True
                if append:
                    to_be_visited = [edge for edge in self.graph_dict[current_vertex].get_edges() if (edge not in path or edge.isupper()) or edge == from_vertex]
                    next_caves += to_be_visited
                else: 
                    path.pop()

            return all_paths


# import input data into graph

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


# Testing

test_paths = cave_system.find_all_paths("start", "end")

print()
print(len(test_paths), "paths found:\n")
for path in test_paths:
   print(path)


# part_paths_from_start = list()
# part_paths_to_end = list()
# for cave in cave_system.graph_dict:
#     if cave.isupper():
#         part_paths_from_start.append(cave_system.find_all_paths("start", cave))
#         part_paths_to_end.append(cave_system.find_all_paths(cave, "end"))

# print(part_paths_from_start)
# print(part_paths_to_end)