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
# for row in cave_map:
#     print(row)


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

# print()
# for key, value in test_graph.graph_dict.items():
#     print(key, " -> ", value.risk_level)

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

# print()
# for key, value in test_graph.graph_dict.items():
#     print(key, " -> ", value.get_edges())   


# find lowest cost path through graph

search_graph = dict()

for vertex in test_graph.graph_dict:
    search_graph[vertex] = [(edge, test_graph.graph_dict[edge].risk_level) for edge in test_graph.graph_dict[vertex].get_edges()]

#print(search_graph)

def dijkstras(graph, start):
  distances = {}
  
  for vertex in graph:
    distances[vertex] = 1000000
    
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

all_distances = dijkstras(search_graph, (0, 0))
#print(all_distances)

print("\nThe path with the total lowest risk has a risk level of", all_distances[len(cave_map)-1, len(cave_map[0])-1])


#****************** Part 2 *****

# enlarge original map 5 times, increasing risk_levels by one

# cave_map = [[int(pos) for pos in line] for line in import_input_data]

print()
for row in cave_map:
    print(row)

def enlarge_map_right(map, times):
    new_map = [[int(pos) for pos in line] for line in map]
    current_tile = map.copy()
    for idx in range(times):
        new_tile = current_tile[:]
        for i in range(len(current_tile)):
            for j in range(len(current_tile[-1])):
                if current_tile[i][j] == 9:
                    new_tile[i][j] = 1
                else:
                    new_tile[i][j] = current_tile[i][j]+1
                new_map[i].append(new_tile[i][j])
        current_tile = new_tile        
    return new_map

enlarged_map_right = enlarge_map_right(cave_map, 4)

def enlarge_map_down(map, times):
    new_map = [[int(pos) for pos in line] for line in map]
    current_tile = map.copy()
    for idx in range(times):
        new_tile = current_tile[:]
        for i in range(len(current_tile)):
            new_map.append([])
            for j in range(len(current_tile[-1])):
                if current_tile[i][j] == 9:
                    new_tile[i][j] = 1
                else:
                    new_tile[i][j] = current_tile[i][j]+1
                new_map[-1].append(new_tile[i][j])
        current_tile = new_tile        
    return new_map

enlarged_map_down = enlarge_map_down(enlarged_map_right, 4)

print()
for row in enlarged_map_down:
    print(row)

enlarged_graph = Graph()

for i in range(len(enlarged_map_down)):
    for j in range(len(enlarged_map_down[0])):
        enlarged_graph.add_vertex(Vertex((i, j), enlarged_map_down[i][j]))

# print()
# for key, value in enlarged_graph.graph_dict.items():
#     print(key, " -> ", value.risk_level)

# add edges

for i in range(len(enlarged_map_down)):
    for j in range(len(enlarged_map_down[0])):
        from_vertex = enlarged_graph.graph_dict[(i, j)]
        if i < len(enlarged_map_down)-1:
            to_vertex_down = enlarged_graph.graph_dict[(i+1, j)]
            enlarged_graph.add_edge(from_vertex, to_vertex_down, to_vertex_down.risk_level)
            if j < len(enlarged_map_down[0])-1:
                to_vertex_right = enlarged_graph.graph_dict[(i, j+1)]
                enlarged_graph.add_edge(from_vertex, to_vertex_right, to_vertex_right.risk_level)
            if j > 0:
                to_vertex_left = enlarged_graph.graph_dict[(i, j-1)]
                enlarged_graph.add_edge(from_vertex, to_vertex_left, to_vertex_left.risk_level)
        if i > 0:
            to_vertex_up = enlarged_graph.graph_dict[(i-1, j)]
            enlarged_graph.add_edge(from_vertex, to_vertex_up, to_vertex_up.risk_level)
        if i == len(enlarged_map_down)-1:
            if j < len(enlarged_map_down[0])-1:
                to_vertex_right = enlarged_graph.graph_dict[(i, j+1)]
                enlarged_graph.add_edge(from_vertex, to_vertex_right, to_vertex_right.risk_level)
            if j > 0:
                to_vertex_left = enlarged_graph.graph_dict[(i, j-1)]
                enlarged_graph.add_edge(from_vertex, to_vertex_left, to_vertex_left.risk_level)
  

# find lowest cost path through graph

enlarged_search_graph = dict()

for vertex in enlarged_graph.graph_dict:
    enlarged_search_graph[vertex] = [(edge, enlarged_graph.graph_dict[edge].risk_level) for edge in enlarged_graph.graph_dict[vertex].get_edges()]


new_distances = dijkstras(enlarged_search_graph, (0, 0))
#print(new_distances)

print("\nThe path with the total lowest risk has a risk level of", new_distances[len(enlarged_map_down)-1, len(enlarged_map_down[0])-1])

