"""
Vasya needs to print out his to-do list for today. Help him: write a function that prints all of his cases.
It is known that Vasya has no more than 5000 cases.
Attention: in this task it is not necessary to read the input data.
You only need to write a function that takes the head of the list as input and prints its elements.
The following is a description of a structure that defines a list node.
"""

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(task_head):
    current = task_head

    while current:
        print(current.value)
        current = current.next_item


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()
