import math
def ghh(n):
    s=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i*i!=n:
                s+=i+n/i
            else: s+=i
    return 2*n<=s
n=int(input())
a=[]
for i in range(n):
    k=int(input())
    if ghh(k):
        a.append(str(k))
print(len(a))
print('\n'.join(a))




