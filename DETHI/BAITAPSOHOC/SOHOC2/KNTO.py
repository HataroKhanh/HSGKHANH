def nguyento(n):
    if n<=1:return False 
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False 
        return True
def uoc(n):
    global a
    dem=0 
    b=[]
    for i in range(1,int(n**0.5)+1):
        if (n%i==0):
            b.append(i)
            if i*i!=n: 
                b.append(n//i)
    return b
# a[2]=1
n=int(input())
a=uoc(n)
print(len([int(i) for i in a if nguyento(i) != 1]))# print(uoc(n))
