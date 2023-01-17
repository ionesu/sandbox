"""
https://contest.yandex.ru/contest/26133/run-report/80914871/

You are given strings packed. Let's define a packed string (CL) recursively.
A string consisting of only lowercase English letters is an ES.
If A and B are correct CSs, then AB is also a CS.
If A is an ES and n is a single-digit natural number, then n[A] is also an ES.
In this case, the notation n[A] means that when unpacking, the string A is written n times in a row.
Find the largest common prefix of the unpacked strings and print it (unpacked).

In other words, let addition be the concatenation of two strings, and multiplying a string by a number is the repetition
of the string the appropriate number of times. Let the function f be able to receive an AP and unpack it.
If ES D has the form D=AB, where A and B are also ESs, then f(D) = f(A) + f(B). If D=n[A], then f(D) = f(A) × n.

Input example:
3
2[a]2[ab]
3[a]2[r2[t]]
a2[aa3[b]]

Time complexity:
O(n*m), where n - number of strings, m - length of longest string
Space complexity:
O(m), where m - length of longest string
"""


def unpack_word(string: str) -> str:
    stack = []

    for char in string:
        if char == '[':
            continue

        if char == ']':
            sequence = []
            prev_char = stack.pop()

            while prev_char and not prev_char.isdigit():
                sequence.append(prev_char)
                prev_char = stack.pop()

            multiplier = int(prev_char) if prev_char else 1
            sequence.reverse()

            stack.append(''.join(sequence) * multiplier)
        else:
            stack.append(char)

    return ''.join(stack)


def max_prefix():
    n = int(input())

    if n == 0:
        return ''

    prefix = unpack_word(input())
    for _ in range(n - 1):
        string = unpack_word(input())

        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

    return prefix


if __name__ == "__main__":
    print(max_prefix())
