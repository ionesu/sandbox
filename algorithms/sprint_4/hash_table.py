"""
https://contest.yandex.ru/contest/24414/run-report/73258003/

Timofey, as a good leader, stores information about the salaries of his employees in the database and constantly updates
 it. He asked you to write an implementation of a hash table to store a database of employee salaries.

The hash table must support the following operations:

put key value - Add a key-value pair. If the given key is already in the table, then the value corresponding to it is
updated.
get key - get value by key. If the key is not in the table, then display "None". Otherwise, display the found value.
delete key -- deleting a key from a table. If there is no such key, then output "None", otherwise output the value
stored by this key and delete the key.
The table stores unique keys.

Implementation requirements:

You cannot use hash table implementations available in programming languages
(std::unordered_map in C++, dict in Python, HashMap in Java, etc.)
Collisions should be resolved using the chaining method or using open addressing.
All operations should be done in O(1) on average.
Support for rehashing and hash table scaling is not required.
Keys and values, employee ids and their salaries are integers. It is not required to support arbitrary hashable types.
Input Format
The first line contains the total number of queries to the table n (1≤ n≤ 106).

The next n lines contain queries, which are of three types - get, put, delete - as described in the condition.

All keys and values are non-negative integers not exceeding 109.

For any sequence of commands, the number of keys in the hash table cannot exceed 105.

Output Format
For each get and delete request, print the answer on a separate line.

Input Example:
10
get 1
put 1 10
put 2 4
get 1
get 2
delete 2
get 2
put 1 5
get 1
delete 2

Operations complexity: average O(1), but worse case could be O(n)
Spatial complexity: O(k)
"""
class HashTable:

    def __init__(self, size):
        self._size = size
        self._slots = [None] * self._size
        self._data = [None] * self._size


    def put(self, key, data):
        slot = self.hash(key)

        if self._slots[slot] is None:
            self._slots[slot] = key
            self._data[slot] = data

        elif self._slots[slot] == key:
            self._data[slot] = data

        else:
            next_slot = self.get_position(self.rehash(slot), key)

            if self._slots[next_slot] is None:
                self._slots[next_slot] = key
                self._data[next_slot] = data

            else:
                self._data[next_slot] = data


    def hash(self, key):
        return hash(key) % self._size


    def rehash(self, old_hash):
        return hash(old_hash + 1) % self._size


    def get(self, key):
        position = self.get_position(self.hash(key), key)
        return self._data[position] if self._slots[position] == key else None


    def get_position(self, position, key):
        while self._slots[position] is not None and self._slots[position] != key:
            position = self.rehash(position)

        return position


    def delete(self, key):
        data = self.get(key)

        if data is not None:
            self.put(key, None)

        return data


def read_commands():
    max_size = int(input())
    hashtable = HashTable(max_size)

    for _ in range(max_size):
        command = input().split()

        if 'get' in command:
            print(hashtable.get(int(command[1])))
        elif 'put' in command:
            hashtable.put(*map(int, command[1:]))
        elif 'delete' in command:
            print(hashtable.delete(int(command[1])))


if __name__ == '__main__':
    read_commands()
