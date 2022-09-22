class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedTasksList:

    def __init__(self):
        self.head = None


    def insert_task(self, value):
        new_node = Node(value)

        if self.head:
            task = self.head

            while task.next:
                task = task.next
            task.next = new_node

        else:
            self.head = new_node


    def print_tasks_list(self):
        task = self.head

        while task:
            print(task.value)
            task = task.next


tasks_list = LinkedTasksList()

for i in range(1, 5000):
    tasks_list.insert_task(f"Task {i}")

tasks_list.print_tasks_list()
