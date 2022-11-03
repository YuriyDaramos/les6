list_1 = [1, "2", 3, [1, 2, 3], [1, 2, [3, [4, 5, [7]]]]]
list_2 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]

list_3 = []

# for el in list_1:
#     if isinstance(el, int):
#         list_3.append(el)
#     else:
#         list_3.extend(el)
#

CONSTANT = (list, set, frozenset, tuple)


def func(start_list, finish_list=None):
    if finish_list is None:
        finish_list = []

    for el in start_list:
        if not isinstance(el, CONSTANT):
            finish_list.append(el)
        else:
            func(el, finish_list)
    return finish_list


result = func(list_1)
pass