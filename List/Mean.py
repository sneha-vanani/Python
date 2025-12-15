#Mean of a list
num = [34,56,79,23,1,29]
sum = 0

for i in num:
    sum += i

print(sum)
print(f"Mean: {sum/len(num)}")
