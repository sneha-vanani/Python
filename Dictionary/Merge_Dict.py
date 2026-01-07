""" Write a python script to merge two dictionaries"""
a = {1:10, 2:20, 3:30}
b = {3:35, 4:40, 5:50}

# a.update(b)
for i in b:
    a[i] = b[i]

print(a)