from math import sqrt
def nt(a):
    if a<=1:return False
    else:
        for i in range(2,int(sqrt(a)+1)):
            if a%i==0:
                return False
        return True
n = int(input())

for x in range(0,int(sqrt(n))+1):
    for y in range(x+1,int(sqrt(n))+1):
        z=x**2+y**2
        if nt(x) and nt(y) and nt(z) and z<=n:
            print(x,y,z,end=" ")
            print()
       
        