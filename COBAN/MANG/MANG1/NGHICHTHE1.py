from collections import defaultdict
n = int(input())
a = map(int,input().split())
f = defaultdict(lambda:0)
for i in a:
    d=0
    for j in f.items():
        if int(j[0])>i:
            d+=j[1]
    print(d,end=' ')
    f[str(i)]+=1
