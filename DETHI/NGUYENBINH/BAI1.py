from math import sqrt
n = int(input())
a = []
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        a.append(i)
        if n!=i*i:
            a.append(n//i)
kmax = 0
for i in a:
    if sqrt(i)==int(sqrt(i)):
       kmax = max(kmax,i)
print(int(sqrt(kmax)),int(n/kmax))