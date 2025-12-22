""" Write a function to flatten a nested list."""

# def flatten(lis):       #flat a list element one level only
#     flat = []
#     i = 0
#     while i < len(lis):
#         # if len(str(lis[i])) > 1:          #older logic
#         if isinstance(lis[i], list):
#             flat.extend(lis[i])
#             i += 1
#         else:
#             flat.append(lis[i])
#             i += 1
#     print(flat)      

def flatten2(lis):
    """this logic is not working becuase i do the changes in list that causes the changes in the length of the list, and the for loop calculates the length only one time when it first time executes"""
    # for i in range(len(lis)):         
    #     print(i)
    #     if isinstance(lis[i], list):
    #         print(i)
    #         lis.extend(lis[i])
    #         lis.pop(i)
    # print("flatten2: ",lis)  

    i=0   
    while i<len(lis):
        print(i)
        if isinstance(lis[i], list):
            lis.extend(lis[i])
            lis.pop(i)
        else: 
            i += 1
    print("flatten2: ",lis)  
    

lis = [2,3, [4,5,6], 7,8,9,[3,[0,0]],'sneha']
# flatten(lis)
flatten2(lis)

