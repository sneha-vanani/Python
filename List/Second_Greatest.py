#Find the second greates elemnt 
num = [34,56,79,23,1,29,70]

""" Older logic"""
# greatest = num[0]
# second_great = num[0]

# for i in num:
#     if i > greatest:
#         second_great = greatest
#         greatest = i
#     elif i > second_great:
#         second_great = i
        
# print(f"Greatest: {greatest} \nthe second greatest elemnt : {second_great}")

"""new logic"""
greatest = max(num)
second_great = max(x for x in num if x != greatest)
print(f"Greatest: {greatest} \nthe second greatest element : {second_great}")