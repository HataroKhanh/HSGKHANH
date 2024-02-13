def nt(n):
    if n<=1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n = int(input())
sdem = 0
a = []
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        if not nt(i):
            a.append(i)
            sdem+=1
        if n!=i*i:
            if not nt(n//i):
                sdem+=1
                a.append(n//i)
print(sdem)
