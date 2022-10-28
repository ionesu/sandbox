"""
Alla really liked the algorithm for calculating a polynomial hash. Help her write a function that computes the hash of
the string s. In this task it is necessary to use their codes in the ASCII table as the values of individual characters.

The polynomial hash is calculated using the formula:

Input Format
The first line contains a number a (1 ≤ a ≤ 1000) – the basis by which the hash is calculated.

The second line contains a number m (1 ≤ m ≤ 109) which is the modulus.

The third line contains a string s (0 ≤ |s| ≤ 106) consisting of uppercase and lowercase Latin letters.

Output Format
Print a non-negative integer - the hash of the given string.

Input Example:
123
100003
a
"""

def polynomial_hash(q: int, R: int, text: str) -> int:
    before_mod = 0
    len_text = len(text)
    x = 1
    for i in text:
        before_mod += ord(i) * (q ** (len_text - x))
        x += 1
    return before_mod % R


def read_input():
    return int(input()), int(input()), input()


if __name__ == '__main__':
    q, R, text = read_input()
    print(polynomial_hash(q, R, text))
