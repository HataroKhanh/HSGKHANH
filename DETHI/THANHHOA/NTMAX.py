import re

def nt(n):
    if int(n)<=1:
        return False
    for i in range(2,int(int(n)**0.5)+1):
        if n%i==0:
            return False
    return True
s = input()
a = re.findall(r'\d+', s)
print(len(re.findall(r'\d', s)))
smax = 0
for i in a:
    if nt(int(i)):
        smax = max(smax,int(i))
print(smax)
