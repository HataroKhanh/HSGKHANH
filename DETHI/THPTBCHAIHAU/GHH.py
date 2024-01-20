def tonguoc(n):
    d = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d+=i
            if n!=i*i:
                d+=n//i
    return d
n = int(input())
a = list(map(int,input().split()))
for i in a:
    if 2*i<=tonguoc(i):
        print(1)
    else:
        print(0)