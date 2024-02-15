from math import comb
n = int(input())
a = list(map(int,input().split()))
c,l = 0,0
for i in a:
    if i%2==0:c+=1
    else:l+=1
#l+c=l
#c+c=c
#l+l=c
sdem = 0
if l%2!=0 and c>=1:
    sdem+= l*c
else:
    sdem += comb(l,2)
    sdem += comb(c,2)
print(sdem)


    
