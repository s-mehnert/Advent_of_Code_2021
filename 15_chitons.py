#***** ADVENT OF CODE 2021 *****
#************ DAY 15 ***********
#****************** Part 1 *****

from heapq import heappop, heappush

# get input data

import_input_data = list()

with open("15_chitons_input.txt") as input:
    for line in input.readlines():
        import_input_data.append(list(line.strip("\n")))

cave_map = [[int(pos) for pos in line] for line in import_input_data]

print()
for row in cave_map:
    print(row)


# create a graph with risk level as weighted edges

class Vertex:
    def __init__(self, value, risk_level=0):
        self.value = value
        self.risk_level = risk_level
        self.edges = dict()
    
    def get_edges(self):
        return list(self.edges.keys())
    
    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight
    
    def get_edge_weight(self, edge):
        return self.edges[edge]

class Graph:
    def __init__(self):
        self.graph_dict = dict()
    
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, risk_level = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, risk_level)


# populate graph with values

test_graph = Graph()

for i in range(len(cave_map)):
    for j in range(len(cave_map[0])):
        test_graph.add_vertex(Vertex((i, j), cave_map[i][j]))

print()
for key, value in test_graph.graph_dict.items():
    print(key, " -> ", value.risk_level)

# add edges

for i in range(len(cave_map)):
    for j in range(len(cave_map[0])):
        from_vertex = test_graph.graph_dict[(i, j)]
        if i < len(cave_map)-1:
            to_vertex_down = test_graph.graph_dict[(i+1, j)]
            test_graph.add_edge(from_vertex, to_vertex_down, to_vertex_down.risk_level)
            if j < len(cave_map[0])-1:
                to_vertex_right = test_graph.graph_dict[(i, j+1)]
                test_graph.add_edge(from_vertex, to_vertex_right, to_vertex_right.risk_level)
            if j > 0:
                to_vertex_left = test_graph.graph_dict[(i, j-1)]
                test_graph.add_edge(from_vertex, to_vertex_left, to_vertex_left.risk_level)
        if i > 0:
            to_vertex_up = test_graph.graph_dict[(i-1, j)]
            test_graph.add_edge(from_vertex, to_vertex_up, to_vertex_up.risk_level)
        if i == len(cave_map)-1:
            if j < len(cave_map[0])-1:
                to_vertex_right = test_graph.graph_dict[(i, j+1)]
                test_graph.add_edge(from_vertex, to_vertex_right, to_vertex_right.risk_level)
            if j > 0:
                to_vertex_left = test_graph.graph_dict[(i, j-1)]
                test_graph.add_edge(from_vertex, to_vertex_left, to_vertex_left.risk_level)

print()
for key, value in test_graph.graph_dict.items():
    print(key, " -> ", value.get_edges())   


# find lowest cost path through graph

search_graph = dict()

for vertex in test_graph.graph_dict:
    search_graph[vertex] = [(edge, test_graph.graph_dict[edge].risk_level) for edge in test_graph.graph_dict[vertex].get_edges()]

print(search_graph)

def dijkstras(graph, start):
  distances = {}
  
  for vertex in graph:
    distances[vertex] = 100
    
  distances[start] = 0
  vertices_to_explore = [(0, start)]
  
  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
        
  return distances

print("\nThe path with the total lowest risk has a risk level of", dijkstras(search_graph, (0, 0))[(9, 9)])

