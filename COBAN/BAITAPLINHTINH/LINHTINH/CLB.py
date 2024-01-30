from collections import defaultdict
n = int(input())
a = map(int,input().split())
f = defaultdict(lambda:0)
for i in a:
    f[str(i)]+=1
ssum = 0
for i in f.items():
    ssum+=int(i[1])//int(i[0])
print(ssum)
