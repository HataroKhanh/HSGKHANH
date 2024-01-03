def step(n,i):
    dem=0
    for j in range(i,n+1,i):
        dem+=1
    return dem        
n = int(input())
a=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        a.append(i)
        if i*i!=n:
            a.append(n//i)
smin = int(10e12)
print(a)
for i in a:
    smin = min(smin,i-1+step(n,i))
    print(i+n-i)
print(smin-1)
