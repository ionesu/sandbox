"""
In order to choose the best algorithm for solving the problem, Gosha continued to study different sorts.
Bubble sort is next - https://en.wikipedia.org/wiki/Bubble_sort

Its algorithm is as follows (sorted in non-decreasing order):

At each iteration, we go through the array, comparing pairs of neighboring elements in turn. If the element at position
i is greater than the element at position i + 1, swap them. After the first iteration, the largest element will
pop up at the end of the array.
We go through the array, performing the specified actions until, at the next iteration, it turns out that the exchanges
are no longer needed, that is, the array has already been sorted.
After no more than n – 1 iterations, the execution of the algorithm ends, since at each iteration at least
one element is in the correct position.

Help Gosha write the code for the algorithm.
Input Format
The first line contains a natural number n — the length of the array, 2 ≤ n ≤ 1000.
The second line contains n space-separated integers.
Each of the numbers does not exceed 1000 in absolute value.

Note that only 2 rows need to be read: the value n and the input array.

Output Format
After each pass through the array, on which some elements are swapped, output its intermediate state.
Thus, if the sorting is completed in k iterations that change the array, then you need to output k lines with n numbers
each — the elements of the array after each of the iterations.
If the array was originally sorted, then just output it.

Input Example:
5
4 3 9 2 1
"""
from typing import List, Tuple
from copy import deepcopy


def bubble_sorting(n: int, array: List[int]):
    for j in range(1, n):
        old_array = deepcopy(array)

        for i in range(n - j):
            element = array[i]
            next_element = array[i + 1]

            if element > next_element:
                array[i + 1] = element
                array[i] = next_element

        if j == 1:
            print(' '.join(map(str, array)))
        elif old_array != array:
            print(' '.join(map(str, array)))


def read_input() -> Tuple[int, List[int]]:
    return int(input()), list(map(int, input().strip().split()))


if __name__ == "__main__":
    n, array = read_input()
    bubble_sorting(n, array)
