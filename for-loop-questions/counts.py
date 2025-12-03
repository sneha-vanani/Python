"""counts the numbers, characters, special symboles of given string"""

str = input("enter a string: ")
digit=0
char=0
schar=0

for i in str:
    if i.isdigit():
        digit +=1
    elif i.isalpha():
        char += 1
    else:
        schar += 1
print(f"digits: {digit} characters: {char} special characters: {schar}")