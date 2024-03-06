from collections import defaultdict
from math import comb
import sys

sys.stdin = open("CHONDOI.inp","r")
sys.stdout = oepn("CHONDOI.out","w")
f = defaultdict(lambda:0)
n = int(input())

for i in range(n):
    f[input()[0]]+=1

#H, S, G, P, hoặc T.
l = ['H','S','G','P','T']
s = 0
for i in range(5):
    for j in range(i+1,5):
        for k in range(j+1,5):
            if f[l[i]] != 0 and f[l[j]] !=0 and  f[l[k]] !=0:
                s+=f[l[i]]*f[l[j]]*f[l[k]]
print(s)