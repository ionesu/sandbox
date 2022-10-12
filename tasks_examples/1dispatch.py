# def string_to_int(str_number: str) -> int:
#     if str_number.isdigit():
#         return int(str_number)
#     else:
#         raise ValueError
#
#
# some_list = ['1', '2', '3']
#
# from typing import List, Any
#
#
# def list_to_int(list_numbers: List[str]) -> int:
#     return string_to_int(''.join(list_numbers))
#
#
# def where_to_pass(data: Any[List, str]) -> int:
#     return list_to_int(data) if isinstance(data, list) else string_to_int(data)
#
# from typing import List

from functools import singledispatch
where_to_pass_cached_values = dict()


@singledispatch
def where_to_pass_new(data):
    pass


@where_to_pass_new.register
def _(str_number: str) -> int:
    if str_number.isdigit():
        return int(str_number)
    else:
        raise ValueError


@where_to_pass_new.register
def _(list_numbers: list):
    if cached_value := where_to_pass_cached_values.get(tuple(list_numbers)):
        return cached_value
    else:
        print(list_numbers)
        where_to_pass_cached_values[tuple(list_numbers)] = where_to_pass_new(''.join(list_numbers))
        return where_to_pass_cached_values[tuple(list_numbers)]


where_to_pass_new(['1', '2', '2'])
where_to_pass_new(['1', '2', '2'])
where_to_pass_new(['1', '2', '2'])
where_to_pass_new(['1', '2', '2'])
where_to_pass_new('123')
