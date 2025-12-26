"""30. Create a function to find unique elements present in only one of two lists."""

def inputLis():
    lis = []
    n = int(input("enter number of values you enter: "))
    print("enter the values: ")
    for _ in range(n):
        i = input()
        lis.append(i)
    return lis

def unique(l1,l2):
    for i in l1:
        if i not in l2:
            print(i,end=' ')
    for i in l2:
        if i not in l1:
            print(i,end=' ')

# def unique(l1,l2):
#     comn = []
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 break

lis1 = inputLis()
lis2 = inputLis()
print("Unique values are: ")
unique(lis1,lis2)