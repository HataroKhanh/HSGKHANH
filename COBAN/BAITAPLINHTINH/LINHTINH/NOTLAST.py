from collections import defaultdict
import sys
f = defaultdict(lambda:0)
n = int(input())
a = []
for i in range(n):
    s,d = map(str,input().split())
    f[s]+=int(d)
smin = min(f.values())
d = 0
kq = ''
check = False
for i,j in f.items():
    if j>smin:
        kq = i
        d+=1
        check = True
        smin = j
    elif j==smin:
        if check == True:
            print(kq)
            sys.exit(0)
    print(d)
if d==1:
    print(kq)
else:
    print('tie')
        
"""
10
Bessie 1
Maggie 13
Elsie 3
Elsie 4
Henrietta 4
Gertie 12
Daisy 7
Annabelle 10
Bessie 6
Henrietta 5
"""