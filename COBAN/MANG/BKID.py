f = {}
n = int(input())
for i in range(1,n+1):
    ip = int(input())
    f[f'{i}']=ip
    
i,j=1,2

while j<n+1:
    if f[str(i)]>f[str(j)]:
        print(str(i))
        i=j;j+=1
    else:
        print(str(j))
        j+=1
    
