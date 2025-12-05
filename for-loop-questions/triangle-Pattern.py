"""*
   **
   ***"""
n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    print()

"""1
   22
   333"""
n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()

"""1
   23
   456"""
n = int(input("Enter a number: "))
k=1

for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k += 1
    print()

"""1
   23
   345
   4567"""
n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i+1):
        print(i+j+1,end=" ")
    print()

"""1
   21
   321
   4321"""
n = int(input("Enter a number: "))

for i in range(n):
    for j in range(i+1):
        print(i-j+1,end=" ")
    print()
    