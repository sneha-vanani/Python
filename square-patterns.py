# """ ****
#     ****
#     ****
#     **** """
# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print("")

# """ 111
#     222
#     333 """
# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n):
#         print(i+1, end=" ")
#     print()

# """ 1234
#     1234
#     1234 """
# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n):
#         print(j+1,end=" ")
#     print()

# """123
#    456
#    789"""
# n = int(input("Enter a number: "))
# k=1

# for i in range(n):
#     for j in range(n):
#         print(k,end=" ")
#         k += 1
#     print()

# """321
#    321
#    321"""
# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n):
#         print(n-j,end=" ")
#     print()

"""AAA
   BBB
   CCC"""

n = int(input("Enter a number: "))
k=65

for i in range(n):  
    for j in range(n):
        print(chr(k),end=" ")
    k += 1 
    print()

"""ABC
   ABC
   ABC"""
n = int(input("Enter a number: "))

for i in range(n):
   for j in range(n):
        print(chr(65 + j),end=' ')

"""ABC
   DEF
   GHI"""
n = int(input("Enter a number: "))
ch = 65

for i in range(n):
   for j in range(n):
        print(chr(ch),end=' ')
        ch += 1
   print()

"""ABC
   BCD
   CDE"""
n = int(input("Enter a number: "))
ch = 65

for i in range(n):
   for j in range(n):
        print(chr(ch + i + j),end=' ')
   print()