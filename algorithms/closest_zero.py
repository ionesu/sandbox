"""
Timothy is looking for a place to build a house for himself. The street he wants to live on has length n, that is,
it consists of n identical consecutive sections. Each plot is either empty or a house has already been built on it.

Sociable Timothy does not want to live far from other people on this street. Therefore, it is important for him to
know for each site the distance to the nearest empty site. If the plot is empty, this value will be equal to zero
- the distance to itself.

Help Timofey calculate the required distances. For this you have a street map. Houses in the city of Timothy were
numbered in the order in which they were built, so their numbers on the map are not ordered in any way.
Empty areas are marked with zeros.

Input example:
5
0 1 4 9 0
"""

from typing import List, Tuple


def closest_zero(n: int, sections: List[int]) -> List[int]:
    distances = []
    previous_zero_position = -1

    for index, section in enumerate(sections):

        if section != 0 and index + 1 == n:
            distances += list(range(1, n - previous_zero_position))
        elif section == 0 and index != 0 and previous_zero_position < 0:
            distances += reversed(list(range(1, index + 1)))
            distances += [0]
            previous_zero_position = index
        elif section == 0 and index - 1 != previous_zero_position >= 0:
            segment = index - previous_zero_position - 1
            segment_module = segment % 2
            half_list = list(range(1, segment // 2 + 1 + segment_module))
            distances += half_list
            distances += half_list[len(half_list) - 1 - segment_module::-1] + [0] if segment > 1 else [0]
            previous_zero_position = index
        elif section == 0:
            distances += [0]
            previous_zero_position = index

    return distances


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return n, arr


n, sections = read_input()
print(' '.join(map(str, closest_zero(n, sections))))


# from typing import List
#
#
# def closest_zero(neighbours: str) -> List[int]:
#     neighbours_list = neighbours.split('0')
#     neighbours_segments_length = len(neighbours_list)
#     distances = []
#     for index, neighbour in enumerate(neighbours_list):
#         segment = len(neighbour)
#
#         if neighbour and index + 1 == neighbours_segments_length:
#             distances += [0] + list(range(1, segment + 1))
#
#         elif neighbour and index == 0:
#             distances += reversed(list(range(1, segment + 1)))
#
#         elif neighbour:
#             segment_module = segment % 2
#             half_list = list(range(1, segment // 2 + 1 + segment_module))
#             distances += [0] + half_list
#             distances += half_list[len(half_list) - 1 - segment_module::-1] if len(half_list) > 1 else []
#
#         elif not neighbour and index != 0:
#             distances += [0]
#
#     return distances
#
#
# def read_input() -> str:
#     n = int(input())
#     arr = str(input().strip().replace(' ', ''))
#     return arr
#
#
# sections = read_input()
# print(' '.join(map(str, closest_zero(sections))))