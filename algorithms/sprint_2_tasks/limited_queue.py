"""
Astrologers have announced a day of limited queues. Timofey needs to write a MyQueueSized class that takes a
max_size parameter, which means the maximum allowable number of elements in the queue.

Help him - implement a program that will emulate the operation of such a queue. The functions to
be supported are described in the input format.

Input Format
The first line contains one number — the number of commands, it does not exceed 5000.
The second line specifies the maximum allowable queue size, it does not exceed 5000.
The commands follow, one per line. Commands can be of the following types:

push(x) - add the number x to the queue;
pop() - remove a number from the queue and print;
peek() - print the first number in the queue;
size() - return the size of the queue;
If the allowed queue size is exceeded, "error" should be displayed. When calling the pop() or peek() operations on
an empty queue, output "None".
Output Format
Print the results of the desired commands, one per line.

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


class MyQueueSized:

    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0


    def is_empty(self):
        return self.size == 0


    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')


    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


    def peek(self):
        return self.queue[self.head]


def read_input():
    num_commands = int(input())
    queue = MyQueueSized(int(input()))

    for i in range(num_commands):
        line = sys.stdin.readline().rstrip()

        if 'push' in line:
            queue.push(int(line.split(' ')[1]))
        elif 'pop' in line:
            print(queue.pop())
        elif 'peek' in line:
            print(queue.peek())
        elif 'size' in line:
            print(queue.size)


if __name__ == "__main__":
    read_input()
