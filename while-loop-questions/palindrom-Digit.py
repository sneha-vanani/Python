num = int(input("enter number:"))
n=num
res=0

while n>0:
    digit = n%10
    res = res * 10 + digit
    n = n // 10

if num == res:
    print(f"palindrom {num}")
else:
    print(f"not palindrom {num}")