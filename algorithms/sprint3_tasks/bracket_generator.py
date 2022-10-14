"""
Rita, on behalf of Timothy, puts things in order in the correct bracket sequences (PSP),
consisting only of parentheses (). To do this, it needs to generate all PSPs of length 2n
in alphabetical order — the alphabet consists of ( and ) and the opening parenthesis comes before the closing one.

Help Rita — write a program that, given n, will output all the PSPs in the required order.

Let's consider the second example. It is necessary to derive the PSP from four characters. There are only two of them:

(())
()()
(()) comes before ()(), since their first character is the same, and the second position of the
first PSP is (, which comes before ).
Input Format
The function takes n as input, an integer from 0 to 10.

Output Format
The function should print all possible bracket sequences of the given length in alphabetical (lexicographical) order.

Input example:
3
"""


def brackets_generator(control, n1, n2, brackets):
    if n1 == 0 and n2 == 0:
        print(brackets)
    else:
        if n1 > 0:
            brackets_generator(control + 1, n1 - 1, n2, brackets + '(')
        if control > 0 and n2 > 0:
            brackets_generator(control - 1, n1, n2 - 1, brackets + ')')


def read_input() -> int:
    return int(input())


if __name__ == "__main__":
    n = read_input()
    brackets_generator(0, n, n, '')
