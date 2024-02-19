def tihon(a):
    ssum = 0
    for i in range(1,int(a**0.5)+1):
        if a%i==0:
            ssum+=i
            if i*i!=a:
                ssum+=n//i
    return a<ssum
n = int(input())
a = list(map(int,input().split()))
d=0
for i in a:
    if not tihon(i):
        d+=1
print(d)