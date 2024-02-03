def nt(n):
    if n<=1:return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
def sodep(n):
    t = str(n)
    
    for i in range(n,0,-1):
        k = int(t[0:i])
        if not nt(int(k)):
            return False
    return True
        
n = int(input())
a = map(int,input().split())
co = False
for i in a:
    if sodep(i):
        co = True
        print(i)
if not co:
    print(0)
