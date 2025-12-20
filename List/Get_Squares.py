"""21. Create a list comprehension to get squares of all even numbers in a range."""

n = int(input("Enter a number till you wants the squares: "))
squar = [(x**2) for x in range(n+1) if x%2 == 0]
print(squar)