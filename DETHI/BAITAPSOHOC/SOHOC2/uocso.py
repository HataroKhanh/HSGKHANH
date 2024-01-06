import sys
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    d=0
    for i in range(1,int((a*b)**0.5)+1):
        if a*b%i==0:
            d+=1
        if ((i*i)!=(a*b)):
            d+=1
    print(d)
