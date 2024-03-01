def cp(n):
    return int(n**0.5)==n**0.5
n = int(input())
d =0
def nt(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(2,n+1):
    if cp(i) and nt(i**0.5):
        d+=1
print(d)