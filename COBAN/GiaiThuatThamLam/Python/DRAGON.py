import sys
n,m=map(int,input().split())
score=n
for i in range(m):
    x,y=map(int,input().split())
    if n>x:
        n+=y
    else:
        print("NO")
        print(m-i)
        sys.exit(0)
print("YES")
