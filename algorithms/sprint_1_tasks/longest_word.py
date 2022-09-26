"""
To prepare for the seminar, Gaucher should read an article on effective management. Since Gosha wants to plan the day
in advance, he needs to estimate the complexity of the article.

He came up with this evaluation method: a random sentence is taken from the text and the longest word is searched for
in it. Its length will be the conditional complexity of the article.

Help Gosha cope with this task.

Input example:
19
i love segment tree
"""

from typing import List, Tuple


def longest_word(a: List[str]) -> Tuple[str, int]:
    word = max(a, key=len)
    return word, len(word)


def read_input() -> List[str]:
    text_length = int(input())
    text = list(map(str, input().strip().split()))
    return text


text = read_input()
print('\n'.join(map(str, longest_word(text))))
