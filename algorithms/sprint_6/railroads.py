"""
https://contest.yandex.ru/contest/25070/run-report/79181102/

There are n cities in country X, which are assigned numbers from 1 to n.
The capital of the country has number n. Railways are laid between the cities.

However, roads can be of two types according to the width of the canvas.
Any train can only travel on one type of track. Conventionally, one type of road is marked as R, and the other as B.
That is, if the route from one city to another has both type R roads and type B roads, then no train will be able
to pass along this route. From one city to another, you can only travel on a route consisting exclusively of type
R roads or only type B roads.

But that's not all. On the roads of country X, you can only move from a city with a lower number to a city with
a higher number. This explains the large influx of residents to the capital, which has the number n.

A railroad map is called optimal if there is no pair of cities A and B such that from A to B can be reached both by
roads of type R and by roads of type B. In other words, for any pair of cities, it is true that from a city with less
number, a city with a higher number can only be reached by roads of one type, or that a route cannot be built at all.
Find out if the card given to you is optimal.

Input example:
4
BBB
RB
B

Output example:
YES

Time complexity: O(V+E)

Space complexity: O(V)
"""

WHITE = 0
GRAY = 1
BLACK = 2

WIDE_ROAD = 'B'
NARROW_ROAD = 'R'


def dfs_is_cyclic(graph, n):
    """
    https://hellokoding.com/detect-cycle-in-a-directed-graph/
    Use a stack to track the traversal path.
    Keeping track of the unvisited (White color), visit in progress (Gray color, the vertex is on the stack)
    and visited state (Black color) of each vertex.
    """
    color = [WHITE] * n
    stack = []

    for i in range(n):
        stack.append(i)

        while stack:
            v = stack[-1]

            if color[v] == WHITE:
                color[v] = GRAY
            else:
                color[v] = BLACK
                stack.pop()

            for w in graph[v]:
                if color[w] == GRAY:
                    return True
                elif color[w] == WHITE:
                    stack.append(w)

    return False


if __name__ == "__main__":
    number_of_cities = int(input())
    neighbours = {city: [] for city in range(number_of_cities)}

    for i in range(number_of_cities - 1):
        for j, road_type in enumerate(input()):
            if road_type == NARROW_ROAD:
                neighbours[i + j + 1].append(i)
            if road_type == WIDE_ROAD:
                neighbours[i].append(i + j + 1)

    print('NO' if dfs_is_cyclic(neighbours, number_of_cities) else 'YES')
