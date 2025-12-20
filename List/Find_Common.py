"""14. Write a function to find common elements in two lists."""

def inputLis():
    lis = []
    n = int(input("enter number of values you enter: "))
    print("enter the values: ")
    for _ in range(n):
        i = input()
        lis.append(i)
    return lis

def common(lis1, lis2):
    cmnLis = []
    for i in lis1:
        for j in lis2:
            if i == j:
                cmnLis.append(i)
    return cmnLis

lis1 = inputLis()
print("For second list")
lis2 = inputLis()

print("The common elements are: ",common(lis1, lis2))


