""" Create a program to count the number of vowels in a string."""
str = input("enter a string: ")
c=0

for i in str:
    if (i == 'A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        c += 1

print(f"the string has {c} vowels")