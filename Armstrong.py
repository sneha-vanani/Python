""" Create a program to print all Armstrong numbers between 1 to 1000.
An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the total number of digits. For example, (153) is an Armstrong number because it has three digits, and (1^{3}+5^{3}+3^{3}) equals (153). Another example is (1634), which is a four-digit number where (1^{4}+6^{4}+3^{4}+4^{4}) equals(1634). """
n = int(input('Enter a number: '))

def armstrong(n1,n2):
   for i in range(1,n2+1):
      num = i
      c = 0
      sum =0

      while num != 0:
         num = num // 10
         c += 1

      num = i
      while num != 0:
         digit = num % 10
         sum += (digit ** c)
         num = num // 10

      if(sum == i):
         print(sum, end='  ')      
   
armstrong(1,n)    