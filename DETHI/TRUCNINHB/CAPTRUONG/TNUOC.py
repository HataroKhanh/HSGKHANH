import sys
#sys.stdin = open("TNUOC.INP","r")
#sys.stdout = open("TNUOC.OUT","w")

n = int(input())
t = 0

if 0<=n<=5:
    t=n*7000
if 5<n<=15:
    t=5*7000+(n-5)*9000
if 15<n<=25:
    t=5*7000+15*9000+(n-20)*11000
if n>25:
    t=5*7000+10*9000+10*11000+(n-25)*15000
print(t//1000,int(t*0.1//1000),int((t+t*0.1)//1000))
