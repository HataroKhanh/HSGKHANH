n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
#
i,j=0,0
smin = float('inf')
while (i<n and j<m):
    smin = min(abs(a[i] + b[j]),smin)
    if j+1<m and abs(a[i] + b[j+1]) <= smin:
        j+=1
    elif i+1<n and abs(a[i+1] + b[j]) <= smin :
        i+=1
    else:break
print(smin)
    
            
    
        