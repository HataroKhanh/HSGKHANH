n = int(input())
smax=0
if 0<n<=5:
    smax=n*7
if 6<n<=15:
    smax=(n-5)*9+5*7
if 16<n<=25:
    smax=(n-15)*11+15*9+5*7
if n>26:
    smax+=(n-25)*15+(25)*11+15*9+5*7
print(smax,int(smax*0.1),smax+int(smax*0.1))
    
