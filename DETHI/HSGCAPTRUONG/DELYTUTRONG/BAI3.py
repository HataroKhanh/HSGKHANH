def nt(a) -> bool:
    if a<=1:return False
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True
n = int(input())
a = [int(i) for i in input().split()]
d=0 
for i in range(0,n):
    if nt(a[i]):
        d+=1
    for j in range(i,n):
        if nt(a[i]+a[j]):
            d+=1
print(d)
