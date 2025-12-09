""" Write a program to print all prime numbers between 1 and 100."""
n1 = int(input("enter starting range: "))
n2 = int(input("enter ending range: "))

for n in range(n1,n2+1):
    if n <= 1:
         continue

    for i in range(2,int(n**0.50)+1):
        if n%i == 0:
            break
    else:
            print(n)