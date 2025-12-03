"""check number is prime or not"""

n = int(input("enter a number: "))

for i in range(2,n+1):
    if n%i == 0:
        if i != n:
            break        


if i == n:
    print(f"the {n} is prime number")
else:
    print(f"the {n} is not prime number")

"""Another way of prime number"""

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    
    return True

n = int(input('enter a number: '))

if is_prime(n):
    print(f'{n} is prime number')
else:
    print(f'{n} is not prime number')