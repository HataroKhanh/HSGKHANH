import sys
sys.stdin = open("LONGFN.inp","r")
sys.stdout = open("LONGFN.out","w")

n = int(input())
if n&1==1:
    print(-(n+1)//2)
else:
    print(m//2)