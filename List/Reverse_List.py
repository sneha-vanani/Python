""" Write a function to reverse a list."""

def rev(li):
    # li.reverse()  #using built-in function
    revl = []
    for i in range(len(li)-1, -1, -1):
        revl.append(li[i])

    print("Reversed list is: ",revl)

li = []
n = int(input("enter number of values you enter: "))
print("enter the values: ")
for _ in range(n):
   i = int(input())
   li.append(i)

rev(li)