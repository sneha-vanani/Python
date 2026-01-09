"""10. Create a dictionary of squares of numbers from 1 to 10"""
n = int(input('enter a number till then you want squares: '))
d = {}

for i in range(1,n+1):
    d[i] = i ** 2
print("Squares: ",d)