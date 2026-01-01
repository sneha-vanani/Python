a = {1,2,False,4,5}
print(a,type(a))

#Add items
x = {'apple','banana','cherry'}
x.add('orange')
print(x)

y = {'pineapple','blackcurrent'}
x.update(y)
print(x)

# print(hash('a'))

#Remove items
x.remove('blackcurrent')        #this will give error if specified item dosn't exist
print(x)

x.discard('kiwi')               #this will NOT give error if specified item dosn't exist
print(x)

x.pop()                           #this will pop random item
print(x)

x.clear()
print(x)

del x

#join methods
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

a.intersection_update(b)
print(a)

"""13. Create a set and perform union, intersection, and difference"""
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a,'\n',b)

# b = set(input('enter set items:'))    #input not working properly
op = int(input('1. Union \n2. Intersection \n3. Difference \nEnter yout choice: '))
match op:
    case 1: 
        res = a.union(b)
        print(res)
    case 2:
        res = a.intersection(b)
        print(res)
    case 3:
        res = a.difference(b)
        print(res)

#Symmetric difference
c = a.symmetric_difference(b)
print('Symmetric difference: ',c)

#Frozen set 
x = frozenset({'apple', 'banan', 'cherry'})
print(x)
print(type(x))

