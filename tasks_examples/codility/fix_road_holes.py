"""
Codility Road fix task
"""


def solution(S):
    holes = 0
    i = 0
    k = len(S)

    # count potholes, ignoring any potholes that are 1 or 2 'to the right' of a pothole we fixed
    while i < k:

        if S[i] == 'X':
            holes += 1
            i += 3

        else:
            i += 1

    return holes


if __name__ == '__main__':
    test1 = solution('.X..X')
    test2 = solution('X.XXXXX.X.')
    test3 = solution('.X.')
    print(test1, test1 == 2)
    print(test2, test2 == 3)
    print(test3, test3 == 1)
