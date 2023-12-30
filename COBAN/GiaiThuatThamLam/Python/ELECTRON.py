import sys
n,m = map(int,input().split())
a = [int(i) for i in input().split()]
if m==1:
    print(1)
    sys.exit(0)
a.sort(reverse=True)
i=0
while m>0 and i<n:
    if m>=a[i]:
        m-=a[i]-1
        i+=1
    else:
        i+=1
        break
print(i if i<n else -1)
