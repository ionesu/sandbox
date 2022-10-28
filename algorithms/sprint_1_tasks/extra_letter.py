"""
Vasya really likes problems about strings, so he came up with his own. There are 2 strings s and t, consisting only of
lowercase letters. The string t is obtained by mixing the letters of the string s and adding 1 letter at a
random position. You need to find the added letter.

Input Format
The input is strings s and t, separated by a line break. Line lengths do not exceed 1000 characters.
Lines are not empty.

Output Format
Remove the extra letter.

Input Example:
abcd
abcde
"""
from typing import Tuple
from collections import Counter


def extra_letter(first:str, second:str) -> str:
    return list((Counter(second) - Counter(first)).keys())[0]


def read_input() -> Tuple[str, str]:
    return input(), input()


if __name__ == '__main__':
    first, second = read_input()
    print(extra_letter(first, second))
