def snn(n):
    a=[]
    for i in range(n):
        b=str(i)
        c=i[::-1]   
        if int(c)+int(b)==n:a.append(i)
    return a
n=int(input())
a=[]
c=[0]*10
for i in range(n):
    x=int(input())
    a.append(x)
for i in a:
    print(len(snn(i)))