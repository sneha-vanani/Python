""" Create a program to print the Fibonacci series up to N terms."""
def fibo(n):
    a = 0
    b = 1
    f = 0

    print(a," ",b,end="   ")
    for i in range(1,n-1):
        f = a + b
        print(f,end="   ")
        a = b
        b = f

n = int(input("Enter the number, which term of fibonacci numbers you want: "))
fibo(n)
