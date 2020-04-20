"""
Depth First Search or DFS for a Graph
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array.

For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0, we look for all
adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don’t mark visited vertices, then 2 will be
processed again and it will become a non-terminating process. A Depth First Traversal of the following graph is 2, 0,
1, 3.
https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

"""
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)


# Create a graph given
# in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)


def perform_DFS(graph, initial_vertex, output_stream):
    adjacent_nodes = graph.graph[initial_vertex]
    output_stream.append(initial_vertex)
    if len(adjacent_nodes) != 0:
        for node in adjacent_nodes:
            if not output_stream.__contains__(node):
                perform_DFS(graph, node, output_stream)
        return output_stream
    else:
        return output_stream


def DFS(graph, starting_vertex):
    my_output_stream = []

    return perform_DFS(graph, starting_vertex, my_output_stream)


print(DFS(g, 2))
