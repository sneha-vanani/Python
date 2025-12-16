#Find the second greates elemnt 
num = [34,56,79,23,1,29,70]
greatest = num[0]
second_great = num[0]

for i in num:
    if i > greatest:
        second_great = greatest
        greatest = i
    elif i > second_great:
        second_great = i
        

print(f"Greatest: {greatest} \nthe second greatest elemnt : {second_great}")
