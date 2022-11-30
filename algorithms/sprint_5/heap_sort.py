"""
In this task, it is necessary to implement heap sort. In this case, the heap must be implemented independently;
it is impossible to use the implementations available in the language.
First, it is recommended to solve problems about sifting down and up.

Timofey decided to organize a sports programming competition to find talented interns.
Tasks are selected, participants are registered, tests are written.
It remains to figure out how the winner will be determined at the end of the competition.

Each participant has a unique login. When the competition ends, two indicators will be attached to it:
the number of solved problems Pi and the size of the penalty Fi.
The penalty is calculated for unsuccessful attempts and time spent on the task.

Timofey decided to sort the table of results in the following way: when comparing two participants,
the one with more problems solved will go higher. If the number of solved problems is equal,
the participant with the lowest penalty goes first. If the penalties are the same, then the first
one will be the one whose login comes earlier in alphabetical (lexicographical) order.

Timofey ordered sweatshirts for the winners and went to the store to pick them up the day before.
In his absence, he commissioned you to implement a Heapsort algorithm for the results table.

Input Example:
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80

Output Example:
gena
timofey
alla
gosha
rita

Time Complexity: O(nlogn)
Space Complexity:O(1)
"""


from dataclasses import dataclass


@dataclass
class User:
    """
    We are using here dataclass  which helps us to generate class code.
    More info - https://habr.com/ru/post/415829/

    When we create objects for classes, it requires memory and the attribute are stored in the form of a dictionary.
    In case if we need to allocate thousands of objects, it will take a lot of memory space.
    slots provide a special mechanism to reduce the size of objects.It is a concept of memory optimisation on objects.
    More info - https://wiki.python.org/moin/UsingSlots
    """

    __slots__ = ['username', 'solved', 'errors']
    username: str
    solved: int
    errors: int

    def key(self):
        return -self.solved, self.errors, self.username

    def __gt__(self, other):
        """
        "Greater than" - means below in the list.
         This user has less Pi, greater Fi, and lesser alphabetical name.
        """

        return self.key() > other.key()

    def __lt__(self, other):
        """
        "Lesser than" - means higher in the list.
         This user has greater Pi, less Fi, and greater alphabetical name.
        """

        return self.key() < other.key()


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr: list):
    n = len(arr)

    for user in range(n // 2, -1, -1):
        # To build a max-heap from any tree, we can thus start heapifying each sub-tree from the bottom up and
        # end up with a max-heap after the function is applied to all the elements including the root element.
        # In the case of a complete tree, the first index of a non-leaf node is given by n/2 - 1.
        # All other nodes after that are leaf-nodes and thus don't need to be heapified.

        heapify(arr, n, user)

    for user in range(n - 1, 0, -1):
        # Remove the root element and put at the end of the array (nth position)
        # Put the last item of the tree (heap) at the vacant place.
        arr[user], arr[0] = arr[0], arr[user]

        # Heapify the root element again so that we have the highest element at root.
        heapify(arr, user, 0)


def read_input_and_create_users():
    n = int(input())
    users = []

    for _ in range(n):
        username, solved, errors = input().split()
        users.append(User(username, int(solved), int(errors)))

    return users


if __name__ == '__main__':
    users = read_input_and_create_users()
    heapsort(users)

    for user in users:
        print(user.username)
