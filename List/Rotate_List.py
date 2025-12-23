"""26. Create a function to rotate a list left by k positions."""

def rotate(lis,k):
    i = 0
    while i < k:
        temp = lis[0]
        lis.pop(0)
        lis.append(temp)
        i += 1
    print("Rotated list: ",lis)

def inputLis():
    lis = []
    n = int(input("enter number of values you enter: "))
    print("enter the values: ")
    for _ in range(n):
        i = input()
        lis.append(i)
    return lis

lis = inputLis()
k = int(input("enter how many times you want to rotate: "))
print("modulo: ",k % len(lis))
rotate(lis,k)