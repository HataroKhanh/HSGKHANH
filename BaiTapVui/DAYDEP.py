from collections import defaultdict
n=int(input())
a=[int(i) for i in input().split()]
d=defaultdict(lambda:0)
for i in a:
    d[f"{i}"]+=1
k=0
for i in d.items():
    if int(i[0])<i[1]:
        k+=i[1]-i[0]
    elif int(i[0])>i[1]:
        k+=i[1]
print(k)
