a,b,c = map(int,input().split())
d = 0
while not (a+1==b and b+1==c):
    if b-a >= c-b:
        c,b = b,b-1
    else:
        a,b = b,b+1
    d+=1
print(d)
        