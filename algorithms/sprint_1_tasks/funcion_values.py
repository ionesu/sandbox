"""
Imagine an online subway game where the player presses a button and three random numbers appear on the screen.
If all three numbers are of the same parity, the player wins.

Write a program that uses three numbers to determine whether a player has won or not.

Input example:
1 2 -3
"""

from typing import List


def function_values(a: List[int]) -> int:
    return a[0]*a[1]*a[1] + a[2]*a[1] + a[3]


def read_input() -> List[int]:
    a = list(map(int, input().strip().split()))
    return a


a = read_input()
print(function_values(a))
