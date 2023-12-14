def snew(s):
    ss=""
    s=s
    back=False
    n=len(s)
    for i in range(n):
        ss+=s[i].lower()
        if s[i].isupper() and i!=0:
            i-=3
            ss=ss[:-1]+'_'
    return ss

        
a=[]    
n=int(input())
for i in range(n):
    ip=input()
    a.append(ip)
for i in a:
    print(snew(i))



