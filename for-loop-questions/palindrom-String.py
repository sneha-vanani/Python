"""check string is palindrom or not"""

str = input("enter a string: ")
rev =""

for i in range(len(str)-1, -1, -1):
    rev += str[i]

if str == rev :
    print(f"'{str}' is palindrome")
else:
    print(f"'{str}' is not palindrome")