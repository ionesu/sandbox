"""
n the company where Timofey works, they take care of the leisure of employees and arrange various circles of interest.
When someone signs up for a class, the name of the circle is entered into the log.

Based on the entries in the log, make a list of all circles that at least one person goes to.

Input Format
The first line contains a natural number n, not exceeding 10 000 - the number of entries in the log.

The next n lines contain the names of circles.

Output Format
Print the unique names of the circles, one per line, in the order they appear in the input.
Input example:
8
cross stitch
drawing with crayons on the desk
table curling
table curling
Horrormay African cuisine
Weightlifting
cockroach science
cockroach science
"""
import sys
from typing import List


def unique_circles(circles: List[str]) -> dict:
    return dict.fromkeys(circles)


def read_input() -> List[str]:
    num_commands = int(input())
    circles = []

    for i in range(num_commands):
        line = sys.stdin.readline().rstrip()
        circles.append(line)

    return circles


if __name__ == '__main__':
    circles = read_input()
    print(*unique_circles(circles), sep="\n")
