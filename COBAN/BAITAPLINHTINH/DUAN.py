n,s=map(int,input().split())
a=[]
for i in range(n):
    v,l=map(int,input().split())
    a.append([v,l])
a=sorted(a,key=lambda x: x[0])
d=0 
for i in a:
    if i[0]<=s:
        s+=i[1]
        d+=1
    else:
        break
print(d)