"""seprate each digit of a number and print it to a new line"""
num = int(input("enter a number:"))

n=num

while n != 0:
    digit = n % 10
    print(digit)
    n = n // 10