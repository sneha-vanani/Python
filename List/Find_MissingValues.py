"""27. Write a function to find the missing number from a list of 1 to N"""

def missing(lst,n):
    mis = []
    for i in range(1,n+1):
        if i not in lst:
            mis.append(i)
    return mis

lst = [1,2,3,4,6,8,9]
n = 9

print(missing(lst,n))

