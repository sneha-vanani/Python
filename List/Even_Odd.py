num = [10,-4,2,79,-1,-67,5]
pos = []
neg = []

for i in num:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
    
print(f"Positive: {pos} \nNegative: {neg}")