"""
https://contest.yandex.ru/contest/25597/run-report/80765537/

The Levenshtein distance between two strings s and t is the number of atomic changes that can be used to turn one string
into another. Atomic changes mean: removing one character, inserting one character, replacing one character with another.

Find the Levenshtein distance for the given pair of strings.

Print a single number — the distance between the lines.

Input example:
abacaba
abaabc

Time complexity:
O(n*m), where m and n - string lengths

Space complexity:
O(n), where n is the length of the shortest string
"""


def levenshtein(str_1: str, str_2: str) -> int:
    n, m = len(str_1), len(str_2)

    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)

    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n

        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]

            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


if __name__ == "__main__":
    print(levenshtein(input(), input()))
