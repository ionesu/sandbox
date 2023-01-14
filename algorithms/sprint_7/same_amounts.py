"""
https://contest.yandex.ru/contest/25597/run-report/80766337/

A table tennis tournament was held on the Algos. Gosha won n games, getting some points for each of them.

Gaucher wondered if it was possible to break all the points he earned during the tournament into two parts so that
the sum of them was the same.

Input example:
4
1 5 7 1

Time complexity:
O(n*s), where n - array, s - sum size

Space complexity:
O(s), where s - sum size
"""


def same_amounts(points: list) -> bool:
    sum_points = sum(points)

    if sum_points % 2 != 0:
        return False

    half_sum = sum_points // 2
    dp = [True] + [False] * half_sum

    for point in points:

        for j in range(half_sum, point - 1, -1):
            dp[j] = dp[j - point] or dp[j]

            if j == half_sum and dp[j]:
                return True

    return dp[-1]


def read_input():
    n = int(input())

    points = list(map(int, input().split()))

    return points


if __name__ == "__main__":
    points = read_input()
    print(same_amounts(points))
