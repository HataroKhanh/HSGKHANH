ax,ay=map(float,input().split())
bx,by=map(float,input().split())
cx,cy=map(float,input().split())

print("YES" if (ax/ay==bx/by==cx/cy) else "No")
