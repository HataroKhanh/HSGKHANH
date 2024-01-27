def nguyento(n):
    if n<=1:return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
def nttn(n):
    check = False
    for i in range(0,10):
        if nguyento(int(str(n)+str(i))):
            check = True
    for i in range(len(str(n))-1):
        if not nguyento(int(str(n)[:(n-i)])):
            check = False
    return check    
        
n = int(input())
a = [int(i) for i in input().split()]
kq = [0]
for i in a:
    if nttn(i):
        kq.append(1)
    else:
        kq.append(0)
kqsum = [0]

for i in range(1,n+1):
    kqsum.append(kqsum[i-1]+kq[i])
b = [[0,0]]
k = int(input())
for i in range(k):
    x,y = map(int,input().split())
    b.append([x,y])
for i in range(1,k+1):
    print(kqsum[b[i][1]]-kqsum[b[i][0]-1])
    

