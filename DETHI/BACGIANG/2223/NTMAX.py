import re

def nt(n):
    if n<=1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n = (input())
num = re.findall(r'\d+',n)
dmax = 0
for i in num:
    if nt(int(i)):
        dmax = max(dmax,int(i))
print(len(num))
print(dmax)