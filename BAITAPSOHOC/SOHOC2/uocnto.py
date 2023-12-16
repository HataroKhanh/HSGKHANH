def san():
    global a
    a[0]=a[1]=0
    for i in range(2,int(10e6)):
        if a[i]:
            for j in range(i*i,int(10e6),i):
                a[j]=0
def khanh(i,j):
    global a
    d=0
    for x in range(i,j+1):
        if a[x]:
            for y in range(2,x+1):
                if x%y==0:
                    d+=1
    return d
a=[1]*int(10e6)
san()
n=int(input())
for i in range(0,n):
    x,y = map(int,input().split())
    print(khanh(x,y))
    
        
