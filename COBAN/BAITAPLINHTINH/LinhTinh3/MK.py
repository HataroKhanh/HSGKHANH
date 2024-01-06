import sys
a,b = map(int,input().split())
# 5 12 93000

s=''
while a>1 and b<=10**a:
    if b>=9:
        s+='9'
        b-=9
    else:
        s+=str(b)
        if len(s)!=a:
            s+='0'*(a-len(s))
            print(s)
            break
    if b>0 and len(s)==a:
        print(-1)
        break
else:
    print(b)