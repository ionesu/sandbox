"""
You need to implement a StackMax class that supports the operation of determining the maximum among all elements
in the stack. The class must support the operations push(x), where x is an integer, pop() and get_max().

Input Format
The first line contains one number n — the number of commands, which does not exceed 10000.
The next n lines contain commands. Commands can be of the following types:

push(x) - push the number x to the stack;
pop() - remove a number from the top of the stack;
get_max() - print the maximum number on the stack;
If the stack is empty, print "None" when calling the get_max() command, and "error" for the pop() command.

Output Format
For each get_max() command, print the result of its execution. If the stack is empty, print
"None" for the get_max() command. If there is a removal from an empty stack, print "error".


Input example:
8
get_max
push 7
pop
push -2
push -1
pop
get_max
get_max
"""

import sys

class StackMax:

    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop() if self.items else print('error')


    def get_max(self):
        return max(self.items) if self.items else None



def read_input():
    stack = StackMax()
    num_commands = int(input())

    for i in range(num_commands):
        line = sys.stdin.readline().rstrip()
        if line == 'get_max':
            print(stack.get_max())
        elif line == 'pop':
            stack.pop()
        elif 'push' in line:
            stack.push(int(line.split(' ')[1]))


if __name__ == "__main__":
    read_input()
