import sys
def san():
    a=[1]*int(10e6)
    a[0]=a[1]=0
    for i in range(2,int(10e6)):
        if (a[i]):
            for j in range(i*i,int(10e6),i):
                a[j]=0
    return a
a=san()
a[2]=1
d=2;
dem=0
ch=True
n=int(input())
while 1:
    if (a[d] and n%d==0):
        n//=d
        if ch:
            dem+=1
            ch=False
    else:
        d+=1;
        ch=True
    if (n==1):break;
print(dem)
