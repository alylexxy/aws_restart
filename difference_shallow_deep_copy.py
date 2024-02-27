import copy

original_dict = {'a': 1, 'b': ["alina", 56], 'c': 3}
copy_dict = dict(original_dict)
deepcopy_dict = copy.deepcopy(original_dict)
original_dict['b'][1]=41

print('Original dictionary')
for key, value in original_dict.items():
    print(f'{key}: {value}')
print('----------')
print('Shallow Copy')
for key, value in copy_dict.items():
    print(f'{key}: {value}')
print('----------')
print('Deep Copy')
for key, value in deepcopy_dict.items():
    print(f'{key}: {value}')