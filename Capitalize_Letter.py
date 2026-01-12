""" Write a function to capitalize the first letter of each word in a string."""
def capitalize(s):
    res = ''
    for i in range(len(s)):
        if i == 0 or s[i-1].isspace():
            res += (s[i]).upper()
        else:
            res += s[i]
    
    print(res)

s = input('enter a string: ')
capitalize(s)