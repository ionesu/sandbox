"""
Timofey decided to buy several houses in the famous Algos archipelago among developers. He found n ads for sale,
where the cost of each house is indicated in Algos francs. And Timothy has k francs.
Help him determine what is the largest number of houses on the Algos he can buy for this money.

Input Format
The first line contains space-separated natural numbers n and k.

n is the number of houses that Timofey considers, it does not exceed 100,000;

k - total budget, does not exceed 100000;

The next line contains n house prices separated by a space. Each of the numbers does not exceed 100000.
All values are natural numbers.

Output Format
Print a single number — the maximum number of houses that Timothy can buy.

Input Example:
3 300
999 999 999
"""

import random
from typing import List, Tuple


def partition(array: List[int], pivot: int) -> Tuple[List[int], List[int], List[int]]:
    left = []
    center = []
    right = []
    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            center.append(i)
    return left, center, right


def quicksort(array: List[int]) -> List[int]:
    arr_len = len(array)
    if arr_len < 2:  # базовый случай,
        return array  # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[random.randint(0, arr_len - 1)]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


def property_buying(amount: int, houses_cost: List[int]) -> int:
    total = 0
    houses_to_buy = 0

    for house in houses_cost:
        total += house

        if total > amount:
            break

        houses_to_buy += 1

    return houses_to_buy


def read_input() -> Tuple[int, int, List[int]]:
    n, amount = map(int, input().split())
    houses_cost = list(map(int, input().split()))

    return n, amount, houses_cost


if __name__ == "__main__":
    n, amount, houses_cost = read_input()
    sorted_houses_cost = quicksort(houses_cost)
    print(property_buying(amount, sorted_houses_cost))
