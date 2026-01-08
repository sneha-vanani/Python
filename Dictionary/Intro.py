#check copy functin for dictionary
# a = {'a':10, 'b':20, 'c':[30,31,32]}
# b = a
# b['a'] = 120        # {'a': 120, 'b': 20, 'c': 30}

# ----- copy function -------
# b = a.copy()
# b['a'] = 120           # {'a': 10, 'b': 20, 'c': 30}
# b['c'].append(0)        # {'a': 10, 'b': 20, 'c': [30, 31, 32, 0]}
# print(f'a: {a}')

# ----- Using dict function -------
# print(f'a: {a}')
# b = dict(a)
# b['a'] = 120           # {'a': 10, 'b': 20, 'c': [30, 31, 32]}
# b['c'].append(0)        # {'a': 10, 'b': 20, 'c': [30, 31, 32, 0]}
# print(f'a: {a}')

# # ----- deepcopy function -------
# import copy
# deep = copy.deepcopy(a)
# deep['c'].append(0)
# print(f'a: {a}, \ndeep: {deep}')

""" Create a nested dictionary to represent student records."""
# students = {
#     1 : { 'name': 'X', 'standard':3, 'marks': [45,78,54,67]},
#     2 : {'name': 'Y', 'standard':4, 'marks': [42,90,87,67]},
#     3 : {'name': 'Z', 'standard':6, 'marks': [53,64,78,97]},
# }

# print(students)