"""#check the number is perfect or not"""
n = int(input("enter a number: "))
sum = 0

for i in range(1,n):
    if n%i == 0:
        sum += i

if sum == n:
    print(f"the {n} is perfect number")
else:
    print(f"the {n} is not perfect number")