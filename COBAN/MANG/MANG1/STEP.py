def bacthang(a) -> bool:
    t=-1
    for i in a:
        if int(i)>=t:
            t=int(i)
        else:
            return False
    return True
n = int(input())
a = [i for i in input().split()]
d=0
for i in a:
    if bacthang(i):
        d+=1
print(d) 