"""
Two arrays of numbers of length n are given. Compose one array of length 2n from them, in which the numbers
from the input arrays alternate (first - second - first - second - ...). In this case, the relative order
of the numbers from one array must be preserved.

Input example:
3
1 2 3
4 5 6
"""

from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    c = []
    for x, y in zip(a, b):
        c.extend((x, y))
    return c


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
