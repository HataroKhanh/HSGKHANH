import sys
sys.stdin = open("UOCLE.INP","r")
sys.stdout = open("UOCLE.OUT","w")

n = int(input())
a = list(map(int,input().split()))
d = 0
for i in a:
    if (i**0.5)%1==0:
        d+=1
print(d)
