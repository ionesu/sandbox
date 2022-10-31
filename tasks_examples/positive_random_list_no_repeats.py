import random


def shuffle_func(arr, n):
    for i in range(n):
        random_number = random.randint(0, n - 1)
        value_one = arr[random_number]
        value_two = arr[random_number - 1]

        arr[random_number] = value_two
        arr[random_number - 1] = value_one

    return arr


def generate_random_positiv(n):
    positiv_numbers = list(range(0, n))
    mixed_positiv_numbers = shuffle_func(positiv_numbers, n)
    return mixed_positiv_numbers


def read_input():
    n = int(input())
    return n


if __name__ == '__main__':
    n = read_input()
    print(generate_random_positiv(n))
