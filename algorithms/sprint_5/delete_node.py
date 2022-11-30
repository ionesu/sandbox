"""
https://contest.yandex.ru/contest/24810/run-report/77306308/

Given a binary search tree that stores the keys. Keys are unique integers.
Find a vertex with a given key and remove it from the tree so that the tree remains a valid binary search tree.
If the key is not in the tree, then the tree does not need to be changed.
The input of your function is the root of the tree and the key to be removed.
The function must return the root of the modified tree.
It is impossible to create new peaks (suddenly you really want to).

Time Complexity: O(h)
Space Complexity: O(h)
h - the height of the tree
"""

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False
if LOCAL:
    class Node:

        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def remove(root, key):
    # if root doesn't exist, just return it
    if root is None:
        return root

    # Find the node in the left subtree	if key value is less than root value
    if root.value > key:
        if root.left:
            root.left = remove(root.left, key)

    # Find the node in right subtree if key value is greater than root value,
    elif root.value < key:
        if root.right:
            root.right = remove(root.right, key)

    # Delete the node if root.value == key
    else:
        if root.right and root.left:
            # Find the minimum element in the right subtree and move it to the place of the node to be deleted
            parent_succ = root
            succ = root.right

            while succ.left:
                parent_succ = succ
                succ = succ.left

            if parent_succ.left == succ:
                parent_succ.left = succ.right
            else:
                parent_succ.right = succ.right

            succ.left = root.left
            succ.right = root.right

            return succ

        # If there is no left children delete the node and new root would be root.right
        elif root.left:
            return root.left

        # If there is no right children delete the node and new root would be root.left
        else:
            return root.right

    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()
