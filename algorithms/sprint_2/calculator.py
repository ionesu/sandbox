"""
https://contest.yandex.ru/contest/22781/run-report/71516171/

The task is related to reverse Polish notation. It is used to parse arithmetic expressions.
It is also sometimes called postfix notation.

In postfix notation, the operands are placed before the operator signs.

Example 1:
3 4 +
means 3 + 4 and equals 7

Example 2:
12 5 /
Since the division is integer, the result is 2.

Example 3:
10 2 4 * -
means 10 - 2 * 4 and equals 2

Let's take a closer look at the last example:

The * sign is immediately after the numbers 2 and 4, which means that you need to apply the operation that this sign
denotes to them, that is, multiply these two numbers. As a result, we get 8.

After that, the expression will take the form:

10 8 -

The minus operation must be applied to the two numbers preceding it, that is, 10 and 8. As a result, we get 2.

Let's consider the algorithm in more detail. To implement it, we will use the stack.

To calculate the value of an expression written in reverse Polish notation, you need to read the expression from left to right and follow these steps:

Input character processing:
If an operand is given as input, it is pushed onto the top of the stack.
If an operation sign is given to the input, then this operation is performed on the required number of values
taken from the stack in the order of addition. The result of the performed operation is placed on the top of the stack.
If the input character set is not fully processed, go to step 1.
After the input character set has been completely processed, the result of the expression evaluation is at the top of
the stack. If there are several numbers left on the stack, then only the top element should be displayed.
A note about negative numbers and division: in this problem, division refers to mathematical integer division.
This means that it always rounds down. Namely: if a / b = c, then b ⋅ c is the largest number that does not
exceed a and is simultaneously divisible by b without remainder.

For example, -1 / 3 = -1. Be careful: in C++, Java, and Go, for example, number division works differently.

In the current problem, it is guaranteed that there is no division by a negative number.

Input Format
The single line contains an expression written in reverse Polish notation. Numbers and arithmetic
operations are written with a space.

Operations can be given as input: +, -, *, / and numbers, modulo not exceeding 10000.

It is guaranteed that the value of intermediate expressions in the test data modulo is not more than 50000.

Output Format
Print a single number — the value of the expression.

Input example:
2 1 + 3 *
"""


class Calculator:

    def __init__(self):
        self._items = []


    def push(self, item):
        """
        Check if item is digit and append it to the items, else we get math operator and using
        https://docs.python.org/3/library/functions.html#eval (if we got division change it to floor division) do
        append to items calculation of 2 previous items
        """
        if item.lstrip('-').isdigit():
            self._items.append(item)
        else:
            self._items.append(str(eval(self.pop(-2) + (item if item != '/' else '//') + self.pop(-1))))


    def pop(self, index):
        return self._items.pop(index)


    def peek(self):
        return self._items[-1]


def read_input() -> list:
    return list(input().strip().split())


def process_input(values: list) -> int:
    calculator = Calculator()

    for i in values:
        calculator.push(i)

    return calculator.peek()


if __name__ == "__main__":
    input_values = read_input()
    print(process_input(input_values))
