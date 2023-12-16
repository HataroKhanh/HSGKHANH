p,n,k=map(int,input().split())
for i in range(n+1):
    p-=k*i
print("YES" if p>=0 else f'NO\n{abs(p)}')
