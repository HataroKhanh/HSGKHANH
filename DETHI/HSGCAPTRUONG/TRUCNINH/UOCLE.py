n = int(input())
a = map(int,input().split())

def uoc(n) -> bool:
    d=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d+=1
            if n!=i*i:
                d+=1
    return d%2!=0
d=0
for i in a:
    if uoc(i):
        d+=1
print(d)