n, k = map(int, input().split())
a = [int(i) for i in input().split()]
f = {}
s = 0
f[0]=[-1]
for i in range(n):
    s+=a[i]
    if s-k in f:
        for j in f[s-k]:
            print(a[j+1:i+1])  
    if s not in f:
        f[s]=[]
    f[s].append(i)
print("f:",f)
