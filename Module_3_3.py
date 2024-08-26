def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1, 2)
print_params(7, True, (5, 4, 10))
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [2.54, {'f': 3, 'k': 15}, 'Строка']
values_dict = {'a': 45, 'b': (8, 9, 10), 'c': False}

print_params(*values_list)
print_params(**values_dict)
