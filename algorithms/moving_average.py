"""
Given statistics on the number of requests per second to your favorite recommendation service.
The measurements were carried out for n seconds.
At second i, qi requests arrive.
Apply the moving average method with window length k to this data and print the result.

Input example:
7
1 2 3 4 5 6 7
4
"""

from typing import List, Tuple

def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    current_sum = sum(arr[0:window_size])
    result.append(current_sum / window_size)
    for i in range(0, len(arr) - window_size):
        current_sum -= arr[i]
        current_sum += arr[i + window_size]
        result.append(current_sum / window_size)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
