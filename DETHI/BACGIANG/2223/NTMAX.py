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
sdem  = 0
for i in num:
    sdem += len(i)
    if nt(int(i)):
        dmax = max(dmax,int(i))
print(sdem)
print(dmax)