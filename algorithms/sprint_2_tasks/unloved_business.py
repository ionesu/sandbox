"""
Vasya thinks about what he can not do from the to-do list that he has compiled.
But it seems that all points are very important! Vasya decides to think of a number and delete the
case that goes under this number. The to-do list is presented as a singly linked list. Write a solution function
that takes as input the head of the list and the number of the case to be deleted and returns the head of the updated list.
Attention: in this task it is not necessary to read the input data.
You only need to write a function that takes as input the head of the list and the number of the element
to be removed and returns the head of the updated list.
"""

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(head, index):

    if index == 0:
        new_head = head.next_item
    else:
        prev_node = get_node_by_index(head, index - 1)
        prev_node.next_item = prev_node.next_item.next_item
        new_head = head

    return new_head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()



