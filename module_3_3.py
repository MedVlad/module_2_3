def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(12)
print_params(a=12, b='проба')
print_params(c=False)
print_params(b='ветер', c=False)
print_params(a=18, b='ветер', c=False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [23, True, [1, 2]]
values_dict = {'a': 'Строка', 'b': False, 'c': 54.3}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
