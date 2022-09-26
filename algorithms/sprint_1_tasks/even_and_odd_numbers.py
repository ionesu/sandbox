"""
Imagine an online subway game where the player presses a button and three random numbers appear on the screen.
If all three numbers are of the same parity, the player wins.

Write a program that uses three numbers to determine whether a player has won or not.

Input example:
1 2 -3
"""

from typing import List


def even_and_odd_numbers(a: List[int]) -> str:
    return 'FAIL' if sum([i % 2 for i in a]) in range(1, 3) else 'WIN'


def read_input() -> List[int]:
    a = list(map(int, input().strip().split()))
    return a


a = read_input()
print(even_and_odd_numbers(a))


# from typing import List
#
#
# def even_and_odd_numbers(a: List[int]) -> str:
#     a_sum = sum([i % 2 for i in a])
#     return 'WIN' if a_sum == 0 or a_sum == 3 else 'FAIL'
#
#
# def read_input() -> List[int]:
#     a = list(map(int, input().strip().split()))
#     return a
#
#
# a = read_input()
# print(even_and_odd_numbers(a))