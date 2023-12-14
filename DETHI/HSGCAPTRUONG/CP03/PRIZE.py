import sys
s=input()
n=int(input())

f=defaultdict(lambda:0)
for i in s:
    f[f'{i}']+=1
def khanh(ss):
    global f
    ff=defaultdict(lambda:0)
    for i in ss:
        ff[f'{i}']+=1
    for i in f.items():
        if i[1] > ff[i[0]]:
            return False
    return True
d=0
for i in range(n):
    k=input()
    if khanh(k):
        d+=1

print(d)

