
def khanh(s):
    ss=''
    n=len(s)
    i=0
    while i<n:
        if s[i].isupper() and i!=0:
            ss+='_'+s[i].lower()
        else:
            ss+=s[i].lower()
        i+=1
    return ss
a=[]
n=int(input())
for i in range(n):
    ip=input()
    a.append(khanh(ip))
for i in a:
    print(i)
