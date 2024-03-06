n = int(input())
xmin,ymin = float('inf'),float('inf')
xmax,ymax = 0,0
for i in range(n):
    x,y = map(int, input().split())
    xmax,xmin=max(xmax,x),min(xmin,x)
    ymax,ymin = max(ymax, y),min(ymin, y)
print(max(xmax-xmin,ymax-ymin)**2)
