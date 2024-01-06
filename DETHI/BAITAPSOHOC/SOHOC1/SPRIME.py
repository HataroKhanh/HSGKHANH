

def nt(a):
    if a<=1:return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
def one(a):
    a=str(a)
    while 1:
        a=a[:-1]
        if a=='':
            return True
        if  not nt(int(a)):
            return False
i,j=map(int,input().split())

for k in range(i,j+1):
    if one(k) and nt(k):
        print(k)

