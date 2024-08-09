def print_params(a=1, b = 'строка', c = True):
  print(a, b, c)

print_params()
print_params(2)
print_params(b = 25)
print_params(c = [1, 2, 3])
values_list = [1, 'строка', True]
values_dict = {'a' : False, 'b' : 22.11, 'c' : 'string'}
print('Распакованный list: ')
print_params(*values_list)
print('Распакованный dict: ')
print_params(**values_dict)
values_list2 = [1994, 'Ноябрь']
print()
print_params(*values_list2, 42)
