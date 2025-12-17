"""4. Create a program that removes duplicates from a list."""

num = []
n = int(input("enter number of values you enter: "))
print("enter the values: ")
for _ in range(n):
   i = int(input())
   num.append(i)

num.sort()
i = 0
while i < len(num)-1:
   if num[i] == num[i+1]:
      num.pop(i+1)
   else:
      i += 1

print("the list after removing duplictes: ",num)