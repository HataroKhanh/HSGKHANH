from math import factorial
n = int(input())
ssum = 1
sdem  = 0
i = 1
while 1:
    ssum *= i
    if len(str(ssum))==n:
        sdem+=1
    elif len(str(ssum))>n:
        print(sdem)
        print(i-1)
        break
    i+=1

