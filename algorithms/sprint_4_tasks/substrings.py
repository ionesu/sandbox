"""
The input is a string. It is necessary to determine the length of the
largest substring that does not contain repeated characters.

Input Format
One line consisting of lowercase Latin letters. The string length does not exceed 10,000.

Output Format
Output a natural number — the answer to the problem.

Input Example:
abcabcbb
"""


def substring(text: str) -> int:
    max_s = ''
    cnt = 0
    max_cnt = 0
    begin, end = 0, len(text)-1

    while begin <= end:
        if text[begin] not in max_s:
            max_s += text[begin]
            cnt += 1
        else:
            max_s = max_s[max_s.index(text[begin]) + 1:] + text[begin]
            cnt = len(max_s)

        if cnt > max_cnt:
            max_cnt = cnt

        begin += 1

    return max_cnt


def read_input() -> str:
    return input()


if __name__ == '__main__':
    print(substring(read_input()))
