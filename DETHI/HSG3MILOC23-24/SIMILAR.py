l,r = map(int,input().split())
print(-1 if (r-l)<(9*len(str(r))) else 9*len(str(r)))
