from collections import defaultdict
N,M = map(int,input().split())
f = []
def nt(n):
    if n<=1 :return 0
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return 0
    return 1
while M!=0:
    x,y = map(int,input().split())
    check = False
    for i in f:
        if x in i:
            i.append(y)
            check =True
        elif y in i:
            i.append(x)
            check = True
    if not check:
        f.append([x,y])
        
    M-=1
fsum = [sum(i) for i in f]
sdem = 0
for i in fsum:
    if not nt(i):sdem+=1
print(sdem)

