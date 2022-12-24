"""
https://contest.yandex.ru/contest/25070/run-report/79243374/

Timofey decided to connect all the computers in his company into a single network.
To do this, he came up with the idea of building a minimum spanning tree in order to use resources more efficiently.

But news came from the authorities that the budget allocated for the network turned out to be very large and urgently
needed to be spent. Therefore, Timofey is now interested not in minimum, but in maximum spanning trees.

He instructed you to find the weight of such a maximum spanning tree in an undirected graph that
defines the layout of the office.

E - number of edges
V - number of vertices

Input example:
4 4
1 2 5
1 3 6
2 4 8
3 4 3

Output example:
19

Time complexity: O(E*logV)

Space complexity:
Heap storage - O(n)
Adjacency list - O(E*V)

"""

from heapq import heappush, heappop


def add_vertex(v, graph_edges, not_added, edges):
    for edge, weight in graph_edges:
        if v in not_added:
            heappush(edges, (-weight, edge))

    not_added.remove(v)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]

    for _ in range(m):
        f, t, w = map(int, input().split())
        f -= 1
        t -= 1
        graph[f].append((t, w))
        graph[t].append((f, w))

    not_added = set(range(n))
    edges = []
    maximum_spanning_tree = 0

    add_vertex(0, graph[0], not_added, edges)

    while not_added and edges:
        weight, v = heappop(edges)

        if v in not_added:
            maximum_spanning_tree += abs(weight)
            add_vertex(v, graph[v], not_added, edges)

    print('Oops! I did it again' if not_added else maximum_spanning_tree)
