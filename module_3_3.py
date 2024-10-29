def print_params(a=1, b='ilya', c=True):
    print(a, b, c)


print_params(b = 25)
print_params(c=[1, 2, 3])
print_params(25, 'one', None)
values_list_ = [13, 'onyx', [1, 2, 3]]
print_params(*values_list_)
values_dict_ = {'a': 13, 'b': 'onyx', 'c': [1, 2, 3]}
print_params(**values_dict_)


def append_to_list(item, values_list=None):
    global values_list_
    if values_list is None:
        values_list = [item]


print(*values_list_)
values_list_2 = [54.32, 'Строка']
print(values_list_2, 42)

