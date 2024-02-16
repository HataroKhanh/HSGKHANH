k,n = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse = True)
ssum,d = 0,0
while ssum<k and d<n:
    ssum+=a[d]
    d+=1
if ssum>=k:
    print(d)
else:
    print(0)
    
    