from collections import defaultdict
def khanh(s):
    f = defaultdict(lambda:0)
    for i in s:
        f[i]+=1
    ck = False
    for i,j in enumerate(s):
        if f[j]==1 and j!=' ':
            return i+1
        else:
            ck = True
    if ck:return -1
n = int(input())    
for i in range(n):
    s = input()
    print(khanh(s))