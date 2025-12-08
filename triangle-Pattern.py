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

"""A
   BB
   CCC"""
n = int(input("Enter a number: "))
ch = 65

for i in range(n):
   for j in range(i+1):
        print(chr(ch + i),end=' ')
   print()
    
"""A
   BC
   DEF
   GHIJ"""
n = int(input("Enter a number: "))
k = 65

for i in range(n):
   for j in range(i+1):
        print(chr(k),end=' ')
        k += 1
   print()

"""A
   BC
   CDE
   DEFG"""
n = int(input("Enter a number: "))
k = 65

for i in range(n):
   for j in range(i+1):
        print(chr(k + i + j),end=' ')
   print()

"""D
   CD
   BCD
   ABCD"""
n = int(input("Enter a number: "))
k = 65

for i in range(n):
   for j in range(i+1):
        print(chr(k + n - i + j - 1),end=' ')
   print()

"""   *
     **
    ***
   ****"""
n = int(input("Enter a number: "))

for i in range(n):
   for s in range(n-i+1):
      print(end=' ')

   for j in range(i+1):
        print('*',end='')
   print()

"""****
   ***
   **
   *"""
n = int(input("Enter a number: "))

for i in range(n):
   for j in range(n-i):
        print('*',end=' ')
   print()

"""****
    ***
     **
      *"""
n = int(input("Enter a number: "))

for i in range(n):
   for s in range(i):
      print(end=' ')

   for j in range(n-i):
        print('*',end='')
   print()

"""   1
     121
    12321
   1234321"""
n = int(input("Enter a number: "))

for i in range(n):
   for s in range(n-i+1):
       print(end=' ')

   for j in range(i+1):
        print((j+1),end='')

   for k in range(i):
       print((i-k), end='')
   print()

"""dabangg pattern :-
1234554321
1234**4321
123****321
12******21
1********1"""
n = int(input("Enter a number: "))

for i in range(n):
   for j in range(n-i):
        print(j+1,end=' ')
   
   for s in range(i):
       print('* *',end=' ')

   for k in range(n-i):
       print((n-i-k),end=" ")
   print()

"""  *
    * *
   * * *       
    * *
     * """
n = int(input("Enter a number: "))

for i in range(1,n+1):
   for s in range(n - i):
         print(end=' ')

   for j in range(i):
        print('*',end=' ')
   print()

for i in range(i-1, 0, -1):
   for s in range(n - i):
      print(end=' ')

   for j in range(i):
      print('*',end=' ')
   print()
    
"""
*********
 *******
  *****
   ***
    * """
n = int(input("enter a number: "))

for i in range(n):
   for s in range(i):
      print(end=' ')

   for j in range(n-i):
      print('*',end='')

   for k in range(n - (i +1)):
      print('*',end='')
   print()

"""   
   *
  **
 ***
****
 ***
  **
   * """
n = int(input("enter a number: "))

for i in range(n):
   for s in range(n-(i+1)):
      print(end=' ')

   for j in range(i+1):
      print('*',end='')
   print()

for k in range(i, 0, -1):
   for s in range(n-k):
      print(end=' ')

   for j in range(k):
      print('*',end='')
   print()