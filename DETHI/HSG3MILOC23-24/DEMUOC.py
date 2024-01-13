n = int(input())
d=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        d+=1
        if i*i!=n:
            d+=1
print(d)