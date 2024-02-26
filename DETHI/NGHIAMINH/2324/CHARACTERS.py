from collections import defaultdict
s = input().split()
f = defaultdict(lambda:0)

for i in s:
    ff = defaultdict(lambda:0)
    for j in i:
        ff[j.lower()]+=1
    d = 0
    for j in ff.values():
        if j == 1:
            d+=1
    f[i] = d
    print(f)
d = max(f.values())
for i,j in ff.items():
    if j == d:
        print(i,end = ' ')

    
        