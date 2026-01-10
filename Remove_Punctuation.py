""" Write a function to remove all punctuation from a string."""
s = input('enter a string: ')
res = ''

for i in s:
    if i.isalnum() or i.isspace():
        res += i
print(res)