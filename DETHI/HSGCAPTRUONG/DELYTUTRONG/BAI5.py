
n = int(input());a=[]
for i in range(n):
    x,y = map(int,input().split())
    a.append([x,y])
def tong(a):
    a=[[0,0]]+a 
    s=0
    for i in range(1,n+1):
        s+=a[i][0]*(i-1)+a[i][1]*(n-1)
    return s+

a1=sorted(a,key=lambda x:x[0])
a2=sorted(a,key=lambda x:x[0],reverse=True)
a3 = sorted(a,key=lambda x:x[1],reverse=True)
a4=sorted(a,key=lambda x:x[1])
print(tong(a1),tong(a2),tong(a3),tong(a4))
         
