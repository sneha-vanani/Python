"""12. Create a program to check if a key exists in a dictionary"""

a = {'a':100, 'b':200, 'c':300, 'd':400, 'e':500}
print(f'Dictionary: {a}')
key = input('enter key you want to search in dictionary: ')

if key in a:
    print(f'"{key}" exists')
else:
    print(f'"{key}"  not exists')
