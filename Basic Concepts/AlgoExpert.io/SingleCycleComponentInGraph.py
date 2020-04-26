"""Number of single cycle components in an undirected graph Given a set of ‘n’ vertices and ‘m’ edges of an
undirected simple graph (no parallel edges and no self-loop), find the number of single-cycle-components present in
the graph. A single-cyclic-component is a graph of n nodes containing a single cycle through all nodes of the
component.

https://www.geeksforgeeks.org/number-of-simple-cyclic-components-in-an-undirected-graph/
"""
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start_vertex, end_vertex):
        self.graph[start_vertex].append(end_vertex)

    def add_edge_list(self, start_vertex, edge_list):
        for edge in edge_list:
            self.graph[start_vertex].append(edge)


my_graph = Graph()

my_graph.add_edge(1, 5)
my_graph.add_edge(1, 10)
my_graph.add_edge(2, 9)
my_graph.add_edge(2, 12)
my_graph.add_edge(2, 15)
my_graph.add_edge(3, 7)
my_graph.add_edge(3, 14)
my_graph.add_edge(5, 1)
my_graph.add_edge(5, 10)
my_graph.add_edge(6, 11)
my_graph.add_edge(6, 14)
my_graph.add_edge(7, 3)
my_graph.add_edge(7, 11)
my_graph.add_edge(8, 13)
my_graph.add_edge(9, 2)
my_graph.add_edge(9, 15)
my_graph.add_edge_list(10, [1, 5])
my_graph.add_edge_list(11, [6, 7])
my_graph.add_edge_list(12, [2, 15])
my_graph.add_edge(13, 8)
my_graph.add_edge_list(14, [3, 6])
my_graph.add_edge_list(15, [2, 9, 12])


def perform_DFS(graph, v, current_graph):
    current_graph.append(v)
    for edge in graph[v]:
        if edge not in current_graph:
            perform_DFS(graph, edge, current_graph)
    return current_graph


def DFS(graph):
    visited_vertices = []
    cycle = []

    for vertex in graph:
        current_graph = []
        if vertex not in visited_vertices:
            current_graph = perform_DFS(graph, vertex, current_graph)
            flag = 0
            for u in current_graph:
                if len(graph[u]) != 2:
                    flag = 1
                    break
            if flag == 0:
                cycle.append(current_graph)
            for k in range(len(current_graph)):
                visited_vertices.append(current_graph[k])
    return cycle


print(DFS(my_graph.graph))
