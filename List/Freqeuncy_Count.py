""" Write a function to count the frequency of elements in a list."""

def count(original):
    original.sort()
    c = 1

    print("Frequency count : ")
    for i in range(len(original)):
        if i == len(original)-1:
            print(f"{original[i]}: {c}")
        elif original[i] == original[i+1]:
            c += 1
        else:
            print(f"{original[i]}: {c}")
            c = 1

num = []
n = int(input("enter number of values you enter: "))
print("enter the values: ")
for _ in range(n):
   i = int(input())
   num.append(i)

count(num)


