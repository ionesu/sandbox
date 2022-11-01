"""
Alla wanted to have narrow flower beds with tulips under her window. On the diagram of the land plot, flower beds
are indicated simply by horizontal segments lying on one straight line. n gardeners were hired for landscaping.
Each of them processed some segment on the diagram. The process was not very well organized, sometimes the same
segment or part of it could be processed by several gardeners at once. Thus, the segments cultivated by two
different gardeners merge into one. The continuous processed segment will then become a flower bed. It is necessary
to determine the boundaries of future flower beds.
Consider examples.
Example 1:
Two identical segments [7,8] and [7,8] merge into one, but then they are covered by the segment [6,10].
Thus, we have two flowerbeds with coordinates [2,3] and [6,10].
Example 2
The segments [2,3], [3,4] and [3,4] merge into one segment [2,4].
The segment [5,6] is not combined with anyone, we add it to the answer.

Input Format
The first line contains the number of gardeners n. The number of gardeners does not exceed 100,000.
The next n lines contain space-separated coordinates of the flowerbeds in the following format: start end, where
start is the start coordinate, end is the end coordinate. Both numbers are integers, non-negative and do not
exceed 107. start is strictly less than end.

Output Format
You need to display the coordinates of each of the resulting flower beds in separate lines.
The data should be displayed in sorted order - first the flowerbeds with smaller coordinates, then - with larger ones.

Input Example:
4
7 8
7 8
2 3
6 10
"""
from typing import Tuple, List


def flowerbed(n: int, coordinates: List[Tuple[int]]) -> List[str]:
    flowerbeds = []
    start = coordinates[0][0]
    end = coordinates[0][1]

    for i in range(n - 1):
        if end < coordinates[i + 1][0]:
            flowerbeds.append('{} {}'.format(start, end))
            start = coordinates[i + 1][0]
            end = coordinates[i + 1][1]

        elif coordinates[i + 1][1] > end:
            end = coordinates[i + 1][1]
    flowerbeds.append('{} {}'.format(start, end))

    return flowerbeds


def read_input() -> Tuple[int, List[Tuple[int]]]:
    n = int(input())
    coordinates = []
    for _ in range(n):
        coordinates.append(tuple(map(int, input().split())))

    coordinates.sort()
    return n, coordinates


if __name__ == "__main__":
    n, coordinates = read_input()
    print('\n'.join(flowerbed(n, coordinates)), end='')
