"""
Gosha implemented the Dec data structure, the maximum size of which is determined by a given number.
Methods push_back(x), push_front(x), pop_back(), pop_front() worked correctly. But, if there were many elements
in the deck, the program worked for a very long time. The fact is that not all operations were performed in O(1).
Help Gosh! Write an efficient implementation.

Attention: when implementing, use a ring buffer.

Input Format
The first line contains the number of commands n — an integer not exceeding 100000. The second line contains the number
m — the maximum deque size. It does not exceed 50000. The next n lines contain one of the commands:

push_back(value) - add an element to the end of the deque. If the deque already contains the maximum
number of elements, print "error".
push_front(value) - add an element to the front of the deque. If the deque already contains the
maximum number of elements, print "error".
pop_front() - Display the first element of the deque and remove it. If deque was empty, print "error".
pop_back() - print the last element of the deque and remove it. If deque was empty, print "error".
Value is an integer, modulo not exceeding 1000.
Output Format
Print the result of each command on a separate line.
No output is required for successful push_back(x) and push_front(x) requests.

Input example:
4
4
push_front 861
push_front -819
pop_back
pop_back
"""
import sys


class Deque:

    def __init__(self, n):
        self.deque = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 1
        self.size = 0


    def is_empty(self):
        return self.size == 0


    def push_front(self, value):
        if self.size != self.max_n:
            self.deque[self.head] = value
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            print('error')


    def push_back(self, value):
        if self.size != self.max_n:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')


    def pop_back(self):
        if self.is_empty():
            return 'error'
        else:
            x = self.deque[self.tail - 1]
            self.deque[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_n
            self.size -= 1
            return x


    def pop_front(self):
        if self.is_empty():
            return 'error'
        else:
            head = self.head + 1 if self.head + 1 != self.max_n else 0
            x = self.deque[head]
            self.deque[head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            return x


def read_input():
    num_commands = int(input())
    deque = Deque(int(input()))

    for i in range(num_commands):
        line = sys.stdin.readline().rstrip()

        if 'push_front' in line:
            deque.push_front(int(line.split(' ')[1]))
        elif 'push_back' in line:
            deque.push_back(int(line.split(' ')[1]))
        elif 'pop_back' == line:
            print(deque.pop_back())
        elif 'pop_front' == line:
            print(deque.pop_front())


if __name__ == "__main__":
    read_input()
