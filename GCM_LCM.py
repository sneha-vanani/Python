""" Write a program to find the GCD of two numbers."""
def GCM(a,b):

    while b != 0:
        a,b = b,a%b
    return a

def LCM(a,b):
    gcm = GCM(a,b)
    return (a*b) / gcm

print("GCM: ",GCM(12,18))
print("LCM: ",LCM(12,18))