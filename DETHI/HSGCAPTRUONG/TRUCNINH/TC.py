n = int(input())
a,b = map(int,input().split())
smax = 0
while n!=0:
    if a>=b:
        smax+=a
        a-=1
    else:
        smax+=b
        b-=1
    n-=1
print(smax)
