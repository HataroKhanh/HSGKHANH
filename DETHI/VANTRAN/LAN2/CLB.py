from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))
f = defaultdict(lambda:0)

for i in a:
	f[i]+=1

sdem = 0
for i,j in f.items():
	sdem+=j/i
print(int(sdem)) 
