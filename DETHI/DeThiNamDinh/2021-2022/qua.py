from sys import stdin,stdout
#stdin = open("qua.inp","r")
#stdout = open("qua.out","w")
a = [0]*int(1e6)
smax = int(1e6)
for i in range(1,int(smax**0.5)+1):
    for j in range(i*i,smax,i):
        a[j]+=i
        if j!=i*i:
            a[j]+=j//i

n = int(input())
s = list(map(int,input().split()))
d = 0
b = []
for i in s:
    if a[i]-i==i:
        b.append(i)
        d+=1
print(d)
print(*b)