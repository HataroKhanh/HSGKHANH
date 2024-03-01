from collections import defaultdict as h
p = print
f = h(lambda:0)
n = int(input())
a = list(map(int,input().split()))

for i in a:
    f[i]+=1

d = 0
t = 0
for i in f.values():
    t+=i//3
    d+=i%3
print(t,d,end = ' ')