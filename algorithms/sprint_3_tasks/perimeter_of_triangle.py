"""
Before going to bed, Rita decided to play a game on her phone. An array of integers is given, in which each element
represents the length of a side of a triangle. It is necessary to determine the maximum possible perimeter of a
triangle made up of sides with lengths from a given array. Help Rita finish the game as soon as possible and go to bed.

Recall that three segments with lengths a ≤ b ≤ c can form a triangle if the triangle inequality holds: c < a + b

Let's take an example:
given the lengths of the sides 6, 3, 3, 2. Let's try to choose 6 as the largest side. The triangle inequality cannot
be satisfied, since 3, 3, 2 are left - the maximum sum of them is 6.

Without the six, the remaining three segments already form a triangle with sides 3, 3, 2.
The inequality is true: 3 < 3 + 2. The perimeter is 3 + 3 + 2 = 8.

Input Format
The first line contains the number of segments n, 3≤ n≤ 10000.

The second line contains n non-negative numbers not exceeding 10,000, the lengths of the segments.

Output Format
You need to print one number - the largest perimeter of the triangle.

It is guaranteed that there is always a triple of numbers that can form a triangle.
Input Example:
4
6 3 3 2

"""
from typing import Tuple, List


def perimeter_of_triangle(n: int, segment_lengths: List[int]) -> int:
    for i in range(0, n - 2):
        if segment_lengths[i] < segment_lengths[i + 1] + segment_lengths[i + 2]:
            return segment_lengths[i] + segment_lengths[i + 1] + segment_lengths[i + 2]
        else:
            continue


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    segment_lengths = sorted(list(map(int, input().split())), reverse=True)
    return n, segment_lengths


if __name__ == '__main__':
    n, segment_lengths = read_input()
    print(perimeter_of_triangle(n, segment_lengths))
