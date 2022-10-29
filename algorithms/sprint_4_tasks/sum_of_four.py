"""
Gosha has a favorite number S.
Help him find all the unique quadruples of numbers in the array that add up to the given number S.

Input Format
The first line contains the total number of array elements n (0 ≤ n ≤ 1000).

The second line contains an integer S .

The third line contains the array itself. Each number is an integer and does not exceed 109 in absolute value.

Output Format
In the first line print the number of fours found.

In the following lines print the found fours. Numbers within the same quadruple must be sorted in ascending order.
Between themselves, the fours are ordered lexicographically.

Input Example:
8
10
2 3 2 4 1 10 3 0
"""
from typing import List, Tuple


def sum_of_four(n: int, s: int, numbers: List[int]) -> List[Tuple[int]]:
    """
    Create a dict with key - sum of 2 numbers, value list of tuples with position of 2 numbers.
    Example:
        {5: [(0, 1), (0, 6), (1, 2), (2, 6), (3, 4)],
        4: [(0, 2), (1, 4), (3, 7), (4, 6)],
        6: [(0, 3), (1, 6), (2, 3)],
        3: [(0, 4), (1, 7), (2, 4), (6, 7)],
        12: [(0, 5), (2, 5)],
        2: [(0, 7), (2, 7)],
        7: [(1, 3), (3, 6)],
        13: [(1, 5), (5, 6)],
        14: [(3, 5)],
        11: [(4, 5)],
        1: [(4, 7)],
        10: [(5, 7)]}

    And fin suitable pairs which gives us 's'
    """

    d = {}
    result = set()

    # Range of list indexes except the last one
    for i in range(n - 1):
        # Range of indexes from i + 1 to the end of the list
        for j in range(i + 1, n):
            # Check find the sum of suitable pair
            value = s - (numbers[i] + numbers[j])

            # Continue if we have suitable pair in dictionary
            if value in d:
                for pair in d[value]:
                    x, y = pair

                    if (x != i and x != j) and (y != i and y != j):
                        sum = [numbers[i], numbers[j], numbers[x], numbers[y]]
                        sum.sort()
                        result.add(tuple(sum))

            d.setdefault(numbers[i] + numbers[j], []).append((i, j))

    return list(result)


def read_input() -> Tuple[int, int, List[int]]:
    n = int(input())
    s = int(input())
    numbers = list(map(int, input().split()))
    return n, s, numbers


if __name__ == '__main__':
    n, s, numbers = read_input()
    result = sum_of_four(n, s, numbers)
    print(len(result))
    result.sort()
    for i in result:
        print(' '.join(map(str, i)))
