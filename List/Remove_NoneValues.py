"""28. Write a program to remove all None values from a list."""

lst = [1,2,None,3,4,None,5]

i = 0
while i < len(lst):
    if lst[i] is None:
        lst.pop(i)
    i += 1

print(lst)