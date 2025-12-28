""" Create a tuple and access its elements."""

t = (1,2,3,'a',True,'b',5)

for i in t:
    print(i)

""" Convert a list into a tuple and vice versa."""
lst = ['a','b','c']
print(type(lst))
tple = tuple(lst)
print(type(tple))

lst1 = list(t)
print(type(lst1))

tple = (1,2,3,4,2,5)
tple2 = ('a', 'b')

#changing the element
# tple[0] = 12      #TypeError: 'tuple' object does not support item assignment

#adding tuples
tple += tple2       
print(tple)

#delete
del tple2       

#unpack tuple
n1,*n2,n3 = tple
print(n1)
print(n2)
print(n3)

#Multiplying tuple
mytuple = tple * 2
print(mytuple)

#Methods:
print(tple.count(2))
print(tple.index(2))