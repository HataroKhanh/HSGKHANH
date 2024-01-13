from collections import defaultdict
check = [2,3,5,7,9]
f = defaultdict(lambda:0)
s = input()
d=0
for i in s:
    if int(i) in check:
        f[i]+=1
for i in f:
    print(i,end=" ")
