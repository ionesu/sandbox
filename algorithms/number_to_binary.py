"""
Vasya has implemented a function that converts an integer from decimal to binary.
But it doesn't seem to work out very well.

Try to write a more efficient program.

Do not use the built-in language tools for converting numbers into binary representation.

Input example:
5
"""

def number_to_binary(num: int) -> int:
    binary_number = ''
    dividing_number = num

    while dividing_number > 0:
        binary_number += str(dividing_number % 2)
        dividing_number = dividing_number // 2

    return int(binary_number[::-1]) if num > 0 else 0


def read_input() -> int:
    number = int(input())
    return number


number = read_input()
print(number_to_binary(number))