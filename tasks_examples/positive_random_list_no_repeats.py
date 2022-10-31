"""
Random Numbers
Write a program that accepts as an input an integer N.
The program needs to return N different random positive integers,
such that each integer in the output is less than or equal to N.

For example, for N=3
Valid output for N=3: [1, 2, 3]
Another valid output for N=3 [3, 2,1]
Invalid outputs would be [1, 1, 3] or [2, 4, 1]
"""

import random


def shuffle_func(arr, n):
    for i in range(n):
        random_number = random.randint(0, n - 1)
        value_one = arr[random_number]
        value_two = arr[random_number - 1]

        arr[random_number] = value_two
        arr[random_number - 1] = value_one

    return arr


def generate_random_positiv(n):
    positiv_numbers = list(range(0, n))
    mixed_positiv_numbers = shuffle_func(positiv_numbers, n)
    return mixed_positiv_numbers


def read_input():
    n = int(input())
    return n


if __name__ == '__main__':
    n = read_input()
    print(generate_random_positiv(n))
