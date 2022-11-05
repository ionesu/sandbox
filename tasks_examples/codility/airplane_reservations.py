"""
You are processing plane seat reservations. The plane has N rows of seats, numbered from 1 to N.
There are ten seats in each row (labelled from A to K, with letter I omitted).
"""


def solution(N: int, S: str) -> int:
    if not S:
        return 2 * N

    left, right, mid = set(), set(), set()
    count = 0

    for r in S.split(' '):
        if r[:-1] in left and r[:-1] in right and r[:-1] in mid:
            continue

        # check if reservation in BCDE
        if r[-1] in 'BCDE':
            left.add(r)
        # check if reservation in FGHJ
        if r[-1] in 'FGHJ':
            right.add(r)
        # check if reservation in DEFG
        if r[-1] in 'DEFG':
            mid.add(r)

    for i in (left | right | mid):
        # check if seat not in 'BCDE' and not in 'FGHJ' than 2 families could seat in a row
        if i not in left and i not in right:
            count += 2
        # check if seat not in 'DEFG' than 1 family could seat in a row
        elif i not in mid:
            count += 1
        # check if seat not in 'BCDE' or not in 'FGHJ' than 1 family could seat in a row
        elif i not in left or i not in right:
            count += 1

    # in all other rows 2 families can seat
    count += 2 * (N - len(left | right | mid))

    return count


if __name__ == "__main__":
    test1 = solution(22, "1A 3C 2B 20G 5A")
    test2 = solution(2, "1A 2F 1C")
    test3 = solution(1, "")
    print(test1, test1 == 41)
    print(test2, test2 == 2)
    print(test3, test3 == 2)
