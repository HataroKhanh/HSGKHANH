def san():
    a = [1]*int(1e6)
    a[0]=a[1]=0
    for i in range(int(int(1e6)**0.5)):
        if a[i]==1:
            for j in range(i*i,(int(int(1e6)**0.5)),i):
                a[j]=0
    return a

a = san()
n = int(input())
k = int(input())
for i in range(n+1):
    if sum(map(int,str(i)))==k and a[i]==1:
        print(i)

                           