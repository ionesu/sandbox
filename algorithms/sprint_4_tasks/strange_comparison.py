"""
The inhabitants of the Algos archipelago came up with a new way to compare strings. Two strings are considered equal if
the characters of one of them can be replaced by the characters of the other so that the first string becomes an exact
copy of the second string. In this case, two conditions must be met:

The order of occurrence of characters must be preserved.
The same characters in the first line must match the same characters in the second line. Different symbols - different.
For example, if the string s = "abacaba", then the string t = "xhxixhx" will be equal to it, since all occurrences of
"a" are replaced by "x", "b" -— by "h", and "c" -— to "i". If the first string is s="abc" and the second string is
t="aaa", then the strings will no longer be equal, since different letters of the first string correspond to the same
letters of the second.

Input Format
The first line contains the string s, the second contains the string t. The lengths of both strings do not exceed 106.
Both strings contain at least one character each and consist only of small Latin letters.

Lines can be of different lengths.

Output Format
Print "YES" if the strings are equal (according to the above rules), and "NO" otherwise.

Input Exmaple:
mxyskaoghi
qodfrgmslc
"""
from typing import Tuple


def strange_comparison(string_1: str, string_2: str) -> str:
    if len(string_1) != len(string_2):
        return 'NO'

    if len(set(string_1)) != len(set(string_2)):
        return 'NO'

    letters_dict = {}
    for i in zip(string_1, string_2):
        exists_value = letters_dict.get(i[0])
        if exists_value:
            if exists_value != i[1]:
                return 'NO'
        else:
            letters_dict[i[0]] = i[1]

    return 'YES'


def read_input() -> Tuple[str, str]:
    return input(), input()


if __name__ == '__main__':
    string_1, string_2 = read_input()
    print(strange_comparison(string_1, string_2))
