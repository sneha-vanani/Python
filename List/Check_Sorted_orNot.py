#check the list is sorted or not
def sortedOrNot(li):
    temp =0
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            return False
    return True

num = [34,56,79,23,1,29,70]
n = [1,2,3,4,5]

if sortedOrNot(n):
    print("Sorted !!")
else:
    print("Not sorted")