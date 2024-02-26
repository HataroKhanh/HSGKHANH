def khanh(a,n,k,m):
    d = 0
    s = 0
    v = m*2
    check = True
    for i in a:
        if check:
            v = i+m*2
            check = False
        if i==v:
            d+=1
            check = True
        elif i>v:
            i-=1
            d+=1
            check = True
    print(d)
            
        
n,k = map(int,input().split())
a = []
l,r = 0,0
for i in range(n):
    ip = int(input())
    r = max(r,ip) 
    a.append(ip)
a.sort()



             