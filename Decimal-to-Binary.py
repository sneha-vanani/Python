"""Q26. Convert a decimal number to binary using loops."""
n = int(input("Enter a decmimal number: "))
res = 0
pow = int(n**0.5)
print(pow)

while 2 ** pow > n:
   pow -= 1

#pow=0
# while 2 ** pow <= n:     #older logic
#    pow += 1
# else:
#    pow -= 1

while pow >= 0:
   if res + (2**pow) <= n:
      res += (2**pow)
      print("1",end='')
   else:
      print(0,end='')
   pow -= 1

"""Another logic"""
n = int(input("enter a number:"))
res = 0
c=0

while n != 0:
   bit = n & 1
   res += bit * (10 ** c)
   # print(res)
   n = n >> 1
   c += 1

print(res)