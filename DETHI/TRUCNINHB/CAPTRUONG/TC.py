import sys
sys.stdin = open("TC.INP","r")
sys.stdout = open("TC.OUT","w")

s = 0
n = int(input())
a,b = map(int,input().split())

while n!=0:
    if a<=b:
        s+=b
        b-=1
    else:
        s+=a
        a-=1
    n-=1
print(s)
