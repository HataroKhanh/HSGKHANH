n = int(input())
a = [int(i) for i in input().split()]
b,c,d=[],[],[]
temp=0
for i in range(0,n):
   if a[i]>temp:
       temp = a[i]
   b.append(temp)
   
temp = 0
for i in range(n-1,-1,-1):
    if a[i]>temp:
        temp = a[i]
    c.append(temp)
smax = 0

for i in range(0,n):
    smax = max(smax,2*b[i]-3*a[i]+5*c[i])
print(smax)