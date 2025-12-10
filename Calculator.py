""" Create a calculator app using if-else"""
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
ope = input("enter Operation[+,-,*,/,%]: ")

if ope == '+':
   print(f"result: {n1} + {n2} = {n1 + n2}")
elif ope == '-':
   print(f"result: {n1} - {n2} = {n1 - n2}")
elif ope == '*':
   print(f"result: {n1} * {n2} = {n1 * n2}")
elif ope == '/':
   print(f"result: {n1} / {n2} = {n1 / n2}")
elif ope == '%':
   print(f"result: {n1} % {n2} = {n1 % n2}")
else:
   print("Invalid Operation !")