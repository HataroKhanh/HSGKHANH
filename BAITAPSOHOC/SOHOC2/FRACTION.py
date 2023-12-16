
b,n=map(int,input().split())
dem=0
tu=[]
mau=[]
for m in range(1,2*n+1):
    if b*m*(2*n-m)%n**2==0 and n!=m:
        dem+=1;
        tu.append(float((b*m*(2*n-m))/n**2))
        mau.append(m)
phanso=zip(tu,mau)
for i in tu:
    print(int(i),end=' ')
print()
for i in mau:
    print(i,end=' ')

