"""
https://contest.yandex.ru/contest/22450/run-report/70517932/

The game "Speed typing simulator" is a field of 4x4 keys. In it, at each round, a configuration of numbers and
points appears. Either a dot or a number from 1 to 9 is written on the key.

At time t, the player must simultaneously press all the keys on which the number t is written. Gosha and Timofey
can press k keys each at the same time. If at time t all the necessary keys are pressed, then the players get 1 point.

Find the number of points that Gosha and Timofey can earn if they press the keys together.

Input example:
4
1111
9999
1111
9911
"""

import sys
from typing import Tuple
from collections import Counter


def sleight_of_hand(k: int, board: str) -> int:
    board_keys_to_count = Counter([*board])
    board_keys_to_count.pop('.', None)
    counter = 0
    for key, value in board_keys_to_count.items():
        counter += 1 if value <= 2*k else 0

    return counter


def read_input() -> Tuple[int, str]:
    k = int(input())
    board = ''

    for i in range(4):
        line = sys.stdin.readline().rstrip()
        board += line

    return k, board


k, board = read_input()
print(sleight_of_hand(k, board))