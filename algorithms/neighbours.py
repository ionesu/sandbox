"""
Given a matrix. You need to write a function that for an element returns all of its neighbors. A neighbor is an
element that is one cell away from the current one to the left, right, up, or down. Diagonal elements are not
considered adjacent.

For example, in matrix A, neighboring elements for (0, 0) will be 2 and 0. And for (2, 1) - 1, 2, 7, 7.

Input example:
4
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
"""
import sys
from typing import List, Tuple


def neighbours(num_lines, num_columns, matrix, y, x) -> List[int]:
    neighbours_list = []

    if num_lines > 1:
        if y == 0:
            neighbours_list += [matrix[y+1][x]]
        elif y + 1 == num_lines:
            neighbours_list += [matrix[y-1][x]]
        else:
            neighbours_list += [matrix[y-1][x], matrix[y+1][x]]

    if num_columns > 1:
        if x == 0:
            neighbours_list += [matrix[y][x+1]]
        elif x + 1 == num_columns:
            neighbours_list += [matrix[y][x-1]]
        else:
            neighbours_list += [matrix[y][x-1], matrix[y][x+1]]

    neighbours_list.sort()

    return neighbours_list


def read_input() -> Tuple[int, int, List[List[int]], int, int]:
    num_lines = int(input())
    num_columns = int(input())
    matrix = []

    for i in range(num_lines):
        line = sys.stdin.readline().rstrip()
        matrix.append(list(map(int, line.strip().split())))

    y = int(input())
    x = int(input())
    return num_lines, num_columns, matrix, y, x


num_lines, num_columns, matrix, y, x = read_input()
print(' '.join(map(str, neighbours(num_lines, num_columns, matrix, y, x))))


# if num_lines > 1 and 0 > y+1 < num_lines:
#     neighbours_list += [matrix[y+1][x]]
#
# if num_columns > 1 and 0 > x +1 < num_columns:
#     neighbours_list += [matrix[y][x+1]]
# elif num_lines > 1 and y != 0:
#     neighbours_list += [matrix[y-1][x]]
# elif num_columns > 1 and x != 0:
#     neighbours_list += [matrix[y][x-1]]

# if y + 1 <= num_lines and num_lines > 1:
#     neighbours_list += [matrix[y-1][x]]
#
# if x >= 0 and num_columns != x+1:
#     neighbours_list += [matrix[y][x+1]]
#
# if y >= 0 and num_lines != y+1:
#     neighbours_list += [matrix[y+1][x]]
#
# if x + 1 <= num_columns and num_columns > 1:
#     neighbours_list += [matrix[y][x-1]]
