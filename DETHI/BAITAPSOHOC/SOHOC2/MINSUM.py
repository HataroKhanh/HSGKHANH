from math import gcd,lcm
G,L = map(int,input().split())
smin=int(10e9)
for a in range(G,L+1):
    for b in range(a+1,L+1):
        if gcd(a,b)==G and lcm(a,b)==b:
            smin=min(a+b,smin)
print(smin if smin!=int(10e9) else -1)
