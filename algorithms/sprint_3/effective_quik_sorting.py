"""
https://contest.yandex.ru/contest/23815/run-report/72272686/

Timofey decided to organize a sports programming competition to find talented interns. Tasks are selected, participants
are registered, tests are written. It remains to figure out how the winner will be determined at the end of the
competition.

Each participant has a unique login. When the competition ends, two indicators will be attached to it: the number of
solved problems Pi and the size of the penalty Fi. The penalty is calculated for unsuccessful attempts and time spent
on the task.

Timofey decided to sort the table of results in the following way: when comparing two participants, the one with more
problems solved will go higher. If the number of solved problems is equal, the participant with the lowest penalty goes
first. If the penalties are the same, then the first one will be the one whose login comes earlier in alphabetical
(lexicographical) order.

Timofey ordered sweatshirts for the winners and went to the store to pick them up the day before. In his absence, he
commissioned you to implement a quick sort algorithm for the results table. Since Timothy loves sports programming and
doesn't like wasting RAM, your sorting implementation cannot consume O(n) additional memory for intermediate data
(this modification of quicksort is called "in-place").

How in-place quick sort works
As in the case of normal quicksort, which uses additional memory, you need to select a pivot element (eng. pivot), and
then reorder the array. Let's make it so that at first there are elements that do not exceed the pivot,
and then - greater than the pivot.

The sort is then called recursively on the two resulting parts. It is at the stage of dividing elements into groups in
the usual algorithm that additional memory is used. Now let's figure out how to implement this in-place step.

Suppose we have somehow chosen a reference element. Let's get two pointers left and right, which will initially point to
the left and right ends of the segment, respectively. Then we will move the left pointer to the right until it points
to an element smaller than the reference one. Similarly, we move the right pointer to the left while it is on the
element that exceeds the reference one. As a result, it turns out that to the left of left all elements exactly belong
to the first group, and to the right of right - to the second. Elements with pointers are out of order. Let's swap them
(most programming languages use the swap() function) and advance pointers to the next elements.
We will repeat this action until left and right collide.
The figure shows an example of splitting at pivot=5. The left pointer is blue, the right pointer is orange.

Input Format
The first line contains the number of participants n, 1 ≤ n ≤ 100 000.
Each of the next n lines contains information about one of the participants.
The i-th participant is described by three parameters:

a unique login (a string of small Latin letters no longer than 20)
the number of solved problems Pi
fi fine
Fi and Pi are integers ranging from 0 to 109.
Output Format
For a sorted list of participants, print their logins in order, one per line.
"""
import sys
import random
from typing import Tuple, List, Union


def partition(array: List[List[Union[int, str]]], pivot: List[Union[int, str]]) -> Tuple[List[List[Union[int, str]]], List[List[Union[int, str]]]]:
    left = []
    right = []
    # Order of comparison (solved tasks, penalties, names)
    comparison_order = [1, 2, 0]
    for item in array:
        for j in comparison_order:
            if item[j] < pivot[j]:
                # Only for solved tasks higher number is good, for names and penalties - not
                left.append(item) if j == 1 else right.append(item)
                break
            elif item[j] > pivot[j]:
                right.append(item) if j == 1 else left.append(item)
                break
            else:
                continue

    return left, right


def quicksort(array: List[List[Union[int, str]]]) -> List[List[Union[int, str]]]:
    if len(array) < 2:  # base case
        return array
    else:
        pivot = array[random.randint(0, len(array) - 1)]
        left, right = partition(array, pivot)
        return quicksort(left) + [pivot] + quicksort(right)


def read_input() -> List[List[Union[int, str]]]:
    n = int(input())
    input_result = []
    for _ in range(n):
        line = sys.stdin.readline().rstrip()
        input_result.append([int(v) if v.isdigit() else v for v in line.strip().split()])
    return input_result


if __name__ == "__main__":
    participants = read_input()
    result = quicksort(participants)
    print(*next(zip(*result[::-1])), sep="\n")

