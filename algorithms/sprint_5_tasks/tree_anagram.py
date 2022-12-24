"""
Gosha and Alla play the game "Amazing Trees". Help the children determine if the tree they see is an anagram tree?
A tree is called an anagram if it is symmetrical about its center.


"""


# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:

        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return root1.value == root2.value and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)


def solution(root) -> bool:
    return is_mirror(root.left, root.right)


def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == '__main__':
    test()
