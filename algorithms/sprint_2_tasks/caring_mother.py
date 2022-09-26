"""
Vasya's mother wants to know what her son plans to do and when. Help her: write a solution function that determines the
 index of the first occurrence of the value passed to it as input in the linked list, if the value is present.
Attention: in this task it is not necessary to read the input data. You only need to write a function that takes the
head of the list and the element you are looking for as input, and returns an integer -
the index of the found element or -1.
"""

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:

        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, elem):
    index = 0

    try:

        while node.value != elem:
            node = node.next_item
            index += 1
        return index

    except:
        return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == '__main__':
    test()
