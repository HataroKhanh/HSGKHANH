def khanhnolove(n):
    a = []
    if n<=1:return None
    
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            a.append(i)
            if n!=i*i:
                a.append(n//i)
    return sum(a)

n = int(input())
a = list(map(int,input().split()))
kq = []
for i in a:
    if khanhnolove(i)==i*2:
        kq.append(i)
kq.sort()
print(' '.join(list(map(str,kq))))