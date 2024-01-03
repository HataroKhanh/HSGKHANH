from math import comb
a,b,c,n= map(int,input().split())

print(comb((a+b+c),n)-comb(a,n)-comb(b,n)-comb(c,n)-comb(a+b,n)-comb(b+c,n)-comb(a+c,n))
    

