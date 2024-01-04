from math import comb
a,b,c,n= map(int,input().split())
print(comb((a+b+c),n)-comb((a+c),n)-comb(b,n)-comb(a+b,n))
    

