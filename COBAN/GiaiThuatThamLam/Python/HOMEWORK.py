n,m = map(int,input().split())
a=sorted([int(i) for i in input().split()][:n])
d=0
for i in a:
    if m>=i:
        m+=i
        d+=1
    else:
        break
print(d)
