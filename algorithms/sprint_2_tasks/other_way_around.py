"""
Vasya decided to confuse his mother by doing things in reverse order. H
is to-do list is now stored in a doubly linked list. Write a function that returns a list in reverse order.
Attention: in this task it is not necessary to read the input data. You only need to write a function that takes the
head of a doubly linked list as input and returns the head of a reversed list.
Below is a description of the structure that defines the top of the list.
"""
# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class DoubleConnectedNode:

        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev


def linked_list(task_tail):
    new_node = task_tail
    m = new_node.next
    new_node.next = None
    new_node.prev = m
    while m is not None:
        m.prev = m.next
        m.next = new_node
        new_node = m
        m = m.prev

    return new_node


def solution(node):
    new_node = node
    old_next_node = new_node.next
    new_node.next = None
    new_node.prev = old_next_node

    while old_next_node is not None:
        old_next_node.prev = old_next_node.next
        old_next_node.next = new_node
        new_node = old_next_node
        old_next_node = old_next_node.prev

    node = new_node
    return node


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1


if __name__ == '__main__':
    test()
