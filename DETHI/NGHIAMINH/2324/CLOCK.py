a,b = map(int,input().split())
d = 0
for i in range(0,b):
    for j in range(0,60):
        i = str(i)
        j = str(j)
        if i[0]==i[-1]==j[0]==j[-1]:
            d+=1
            print(i,j)
for i in range(0,b+1):
    a = str(a)
    i = str(i)
    if a[0]==a[-1]==i[0]==i[-1]:
        d+=1
        print(a,i)
print(d)