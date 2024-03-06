from collections import Counter
import sys
sys.stdin = open("DAYDEP.out","w")
sys.stdout = open("DAYDEP.out","r")
n = int(input())
a = list(map(int,input().split()))
b = Counter(a)
s = 0
for i,j in b.items():
    if i>j:
        s+=j
    elif i<j:
        s+=j-i
print(s)