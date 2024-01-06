def nt(n):
    if n<=1:return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    print("YES" if nt(b**2-a**2) else "NO")