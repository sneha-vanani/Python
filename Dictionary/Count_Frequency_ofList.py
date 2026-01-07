"""count the frequency of each element of list"""
lst = [1,1,1,2,2,3,3,3,4,4,4,0,0,5]
d = {}

for i in lst:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)