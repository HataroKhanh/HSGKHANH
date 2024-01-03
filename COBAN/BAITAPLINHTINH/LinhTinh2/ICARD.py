n,m = map(int,input().split())
a="".join(map(str,[int(i) for i in input().split()]))
b=[]
for i in range(m):
    B,C = map(int,input().split())
    b.append([B,C])
b=sorted(b,key=lambda x:x[1],reverse=True)
print(a)
