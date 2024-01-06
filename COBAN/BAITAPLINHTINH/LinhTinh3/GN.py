a,b,c,d = map(int,input().split())

l = max(a,c)
r = min(b,d)
print(0 if r<l else r-l+1)