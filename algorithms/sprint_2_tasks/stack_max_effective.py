"""
Implement a StackMaxEffective class that supports the operation of determining the maximum among the elements on the
stack. The complexity of the operation should be O(1). For an empty stack, the operation must return None.
However, push(x) and pop() must also run in constant time.

Input Format
The first line contains one number — the number of commands, it does not exceed 100000. Then there are commands,
one per line. Commands can be of the following types:

push(x) - push the number x to the stack;
pop() - remove a number from the top of the stack;
get_max() - print the maximum number on the stack;
If the stack is empty, print “None” when calling the get_max command, and “error” for the pop command.
Output Format
For each get_max() command, print the result of its execution. If the stack is empty, print "None" for the get_max()
command. If there is a removal from an empty stack, print "error".


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


class StackMaxEffective:

    def __init__(self):
        self.items = []
        self.max_values = []


    def push(self, item):
        self.items.append(item)
        if not self.max_values or self.max_values[-1] <= item:
            self.max_values.append(item)


    def pop(self):
        if self.items:
            if self.items.pop() == self.max_values[-1]:
                self.max_values.pop()
        else:
            print('error')


    def get_max(self):
        return self.max_values[-1] if self.max_values else None


def read_input():
    stack = StackMaxEffective()
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
