"""29. Write a function to merge two dictionaries and handle key collisions by summing values."""
a = {'a':100, 'b':200, 'c':300}
b = {'c':350, 'd':400, 'e':500}

for i in b:
    if i in a:
        a[i] += b[i]
    else:
        a[i] = b[i]
print(a)