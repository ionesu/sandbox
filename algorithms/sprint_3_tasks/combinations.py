"""
On the keyboard of old mobile phones, each digit corresponded to several letters. More or less like this:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

You know in what order the phone buttons were pressed, excluding repetitions.
Type all combinations of letters that can be typed in such a sequence of clicks.

Input Format
The input is a string consisting of numbers 2-9 inclusive. The string length does not exceed 10 characters.

Output Format
Output all possible combinations of letters separated by spaces.

Input example:
23
"""

VALUES_DICT = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combinations(numbers):
    if not numbers:
        return ['']

    result = []
    word = VALUES_DICT[numbers[-1]]

    for combination in combinations(numbers[:-1:]):
        for c in word:
            result.append(combination + c)

    return result


def read_input() -> str:
    return input()


if __name__ == "__main__":
    clicked = read_input()
    print(' '.join(combinations(clicked)))
