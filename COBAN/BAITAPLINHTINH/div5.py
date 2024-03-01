from collections import defaultdict
def khanh(a,n):
    f = defaultdict(lambda:0)
    for i in a:
        f[i]+=1
    d = 0
    
n = int(input())
for i in range(n):
    ip  = int(input())
    a = list(map(int,input().split()))
    print(khanh(a,n))