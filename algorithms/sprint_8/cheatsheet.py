"""
https://contest.yandex.ru/contest/26133/run-report/80910238/

Vasya is preparing for an exam in algorithms and writes cheat sheets just in case.

To fit as much information as possible on them, he does not separate words with spaces.
The result is one very long line. In order not to get confused in what you read during the exam itself due to nerves,
he asks you to write a program that will determine from this long line and a set of valid words whether
the text can be broken into separate words from the set.

More formally: given a text T and a set of strings s1, ... ,sn. We need to determine whether we can represent T
as sk1sk2...skr, where where ki are row indices. Indexes can be repeated. The string si can appear in the text
break T an arbitrary number of times. It is possible to use not all lines for splitting. The lines can be in any order.

Input example:
examiwillpasstheexam
5
will
pass
the
exam
i

Time complexity:
Prefix tree - O(L), where L — the total length of all words in the set
Iterating through the Prefix tree - O(n^2), where n - number of chars in string
Space complexity:
Prefix tree - O(L), where L — the total length of all words in the set
Array - O(n), where n - number of chars in string
"""


class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = {} if next is None else next
        self.terminal = False


def create_tree(words: list) -> Node:
    root = Node('')

    for word in words:
        node = root

        for index, char in enumerate(word):
            node.next[char] = node.next.get(char, Node(char))
            node = node.next[char]
        node.terminal = len(word)

    return root


def split_words(string: str, words: list) -> bool:
    root = create_tree(words)
    dp = [True] + [False] * len(string)

    for i in range(len(string)):
        node = root

        if dp[i]:

            for j in range(i, len(string) + 1):

                if node.terminal:
                    dp[j] = True

                if j == len(string) or not node.next.get(string[j], False):
                    break

                node = node.next[string[j]]

    return dp[-1]


def read_input() -> tuple:
    string = input()
    words_list = [input() for _ in range(int(input()))]

    return string, words_list


if __name__ == '__main__':
    string, words = read_input()
    print('YES' if split_words(string, words) else 'NO')
