"""
Rita decided to keep only three colors of clothes: pink, yellow and crimson. With the other colors out of the way,
Rita wanted to sort her new wardrobe by color. First, things should go pink, then - yellow, and at the end - raspberry.
Help Rita cope with this task.

Note: Try to solve the problem in one pass through the array!

Input Format
The first line contains the number of items in the wardrobe: n - it does not exceed 1000000.
The second line contains an array that specifies the color for each item. Pink is 0, yellow is 1, magenta is 2.

Output Format
It is necessary to output the colors of objects in the correct order, separated by a space.

Input Example:
7
0 2 1 2 0 0 1
"""


def wardrobe(clothes: list) -> list:
    clothes_quantity = [0, 0, 0]

    for item in clothes:
        clothes_quantity[item] += 1

    sorted_clothes = []

    for color, quntity in enumerate(clothes_quantity):
        sorted_clothes += [color] * quntity

    return sorted_clothes


def read_input() -> list:
    n = int(input())
    clothes = list(map(int, input().split(' '))) if n > 0 else []
    return clothes


if __name__ == "__main__":
    clothes = read_input()
    print(' '.join(map(str, wardrobe(clothes))))
