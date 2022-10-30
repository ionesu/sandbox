"""
In the evening, the guys decided to play the game "Big Number".
Numbers are given. It is necessary to determine what is the largest number that can be formed from them.

Input Format
The first line contains n — the number of numbers. It does not exceed 100.
The second line contains n space-separated non-negative numbers, each of which does not exceed 1000.

Output Format
You need to print the largest number that can be made from the given numbers.

Input example:
3
15 56 2
"""
import functools
from typing import List, Tuple


def cmp(a, b) -> int:
    return -1 if (a[0] * 10 ** len(b[1]) + b[0]) > (b[0] * 10 ** len(a[1]) + a[0]) else 1


def biggest_number(array: List[Tuple]) -> List:
    array.sort(key=functools.cmp_to_key(cmp))
    return array


def read_input() -> List[Tuple]:
    input()
    return [tuple([int(x), x]) for x in input().split(' ')]


if __name__ == "__main__":
    array = read_input()
    print(''.join([x[1] for x in biggest_number(array)]), end='')
