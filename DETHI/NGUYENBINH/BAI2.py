def k(n):
    d = 0
    if n>=1:
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                d+=1
                if i*i!=n:
                    d+=1
    return d
ssum = 0
n = int(input())
a = list(map(int,input().split()))
for i in a:
    ssum+=i*k(i)
print(ssum)



