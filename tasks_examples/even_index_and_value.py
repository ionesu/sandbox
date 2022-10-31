some_list = [1, 2, 3, 5, 8, 6, 10]


def check_even(values):
    new_list = []
    for index, i in enumerate(values):
        if index % 2 == 0 and i % 2 == 0:
            new_list.append(i)
    return new_list


print(check_even(some_list))
