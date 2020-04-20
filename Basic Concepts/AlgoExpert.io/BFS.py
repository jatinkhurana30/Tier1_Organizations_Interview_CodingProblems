"""https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/ Breadth First Search or BFS for a Graph

Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2 of this
post). The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To
avoid processing a node more than once, we use a boolean visited array. For simplicity, it is assumed that all
vertices are reachable from the starting vertex. For example, in the following graph, we start traversal from vertex
2. When we come to vertex 0, we look for all adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don’t
mark visited vertices, then 2 will be processed again and it will become a non-terminating process. A Breadth First
Traversal of the following graph is 2, 0, 3, 1.

"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

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


def BFS(graph, starting_vertex):
    queue = []
    output_stream = []

    queue.append(starting_vertex)

    while len(queue) != 0:
        next_vertex = queue.pop(0)
        if not output_stream.__contains__(next_vertex):
            adjacent_vertices = graph.graph[next_vertex]
            for vertex in adjacent_vertices:
                queue.append(vertex)
            output_stream.append(next_vertex)

    return output_stream


print(BFS(g,2))
