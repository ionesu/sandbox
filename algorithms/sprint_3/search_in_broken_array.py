"""
https://contest.yandex.ru/contest/23815/run-report/72230156/

Alla made a mistake when copying from one data structure to another. She stored an array of numbers in a ring buffer.
The array was sorted in ascending order, and it was possible to find an element in it in logarithmic time.
Alla copied the data from the ring buffer into a regular array, but shifted the data of the original sorted sequence.
Now the array is not sorted. However, it is necessary to provide the ability to find an element in it in O(logn).
It can be assumed that the array contains only unique elements.
The task must be submitted with the Make compiler, it is selected by default, there are no other compilers in the task.
The solution is sent as a file. The required function signatures are in the code stubs on disk.

You are required to implement a function that searches the broken array.
Files with code stubs containing function signatures and a basic test for supported languages can be found on Yandex.
Disk at the link. Note that you do not need to read data and output a response.
The file extension must match the language you are writing in (.cpp, .java, .go, .js, .py).
If you write in Java, name the solution file Solution.java, for C# - Solution.cs. For other languages,
the name can be anything except solution.ext, where ext is the permission for your language.

Input Format
The function takes an array of natural numbers and the desired number
k. The length of the array does not exceed 10000.
The elements of the array and the number k do not exceed 10000 in value.
In the examples:
The first line contains the number n, the length of the array.
The second line contains a positive number k, the required element.
Next, the line contains n natural numbers separated by a space – the elements of the array.

Output Format
The function must return the index of the element equal to k, if there is one in the array (numbering from zero).
If the element is not found, the function should return -1.
The array cannot be changed.
To cut off inefficient solutions, your function will run from 100,000 to 1,000,000 times.

Input example:
9
5
19 21 100 101 1 4 5 7 12

Algorithm complexity O(logn)
"""


def broken_search(nums, target) -> int:
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if nums[mid_index] == target:
            return mid_index

        if nums[left_index] <= nums[mid_index]:
            if nums[left_index] <= target < nums[mid_index]:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
        else:
            if nums[mid_index] < target <= nums[right_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


