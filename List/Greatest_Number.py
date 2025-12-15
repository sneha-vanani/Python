#Find the greatest number and print its index too
num = [34,56,79,23,1,29]
great = num[0]
index = 0

for i in range(len(num)):
    if num[i] > great:
        great = num[i]
        index = i

print(f"Greatest element: {great} \nAt index: {index}")