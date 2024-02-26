def nt(n):
    if n<=1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n,k = map(int,input().split())
a = []
for i in range(k):
    l,r = map(int,input().split())
    check = False
    for j in a:
        if (l in j) or (r in j):
            j.add(r)
            j.add(l)
            check = True
    if not check:
        a.append({l,r})
b = []
for i in a:
    b.append(list(i))
b = sum(b,[])
for i in range(1,n+1):
    if i not in b:
        a.append({i})
d = 0
for i in a:
    if not nt(len(i)):
        d+=1
print(d)
