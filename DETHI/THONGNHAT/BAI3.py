from math import ceil
def nt(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def khanh(n):
    k =  ceil(n**0.5)
    while 1:
        if nt(k):
            return k**2
        k+=1
n = int(input())
print(khanh(n))
