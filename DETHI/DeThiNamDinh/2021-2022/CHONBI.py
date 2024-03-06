import sys
sys.stdin = open("CHONBI.inp","r")
sys.stdout = open("CHONBI.out","w")
m,n = map(int,input().split())
a = []
for i in range(n):
    x,y = map(int,input().split())
    a.append((x,y))
a.sort(key = lambda x:x[1],reverse=True)
s = 0
for i,j in a:
    if m>i:
        s+=i*j
        m-=i
    elif m<=i:
        s+=j*m
        print(s)
        break