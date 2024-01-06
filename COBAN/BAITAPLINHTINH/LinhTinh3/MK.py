a,b = map(int,input().split())
if a==1:print(b)
else:
    for i in range(10**a,10**(a-1),-1):
        if sum([int(i) for i in str(i)]) == b:
            print(i)
            break
