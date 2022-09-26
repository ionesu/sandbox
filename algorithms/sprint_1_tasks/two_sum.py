"""
Rita and Gosha are playing a game. Rita has n pieces, each of which has the number of points written on it.
The chips lie on the table in non-decreasing order of points on them. First, Gosha names the number k, then Rita must
choose two chips, the sum of points on which is equal to the given number.

Rita was tired of looking for chips herself, and she decided to use her programming skills to solve this problem.
Help her write a program to find the chips she needs.

Input example:
6
-9 -7 -6 -1 -1 3
2
"""

from typing import List, Tuple, Optional

def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    arr_set = set()
    for current_number in arr:
        target_number = target_sum - current_number
        if target_number in arr_set:
            return target_number, current_number
        else:
            arr_set.add(current_number)

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
