"""
Write a program that determines whether a positive integer is a power of 4.

Hint: the power of four will be all numbers of the form 4n, where n is a non-negative integer.

Input Format
The input is an integer in the range from 1 to 10000.

Output Format
Print "True" if the number is a power of four, "False" otherwise.

Input Example:
15
"""


def expanention_of_four(number: int) -> bool:
    return True if number in [1, 4] or (number > 0 and (number ** (0.5)) % 4 == 0) else False


def read_input() -> int:
    return int(input())


if __name__ == '__main__':
    print(expanention_of_four(read_input()))
