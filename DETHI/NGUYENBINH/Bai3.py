def ttto(n,a):
    a = [0] + a
    b = [0]
    for i in range(1,n+1):
        b.append(a[i]+b[i-1])
    return b
def khanh(n,a):
    b = ttto(n,a)
    for i in range(1,n+1):
        if (b[n]-b[i-1])==(b[i]-b[0]):
            return i
    return -1
n = int(input())
for i in range(n):
    ip = int(input())
    a = list(map(int,input().split()))
    print(khanh(ip,a))




