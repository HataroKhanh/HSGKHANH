def uoc(s):
    n = len(s)
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            a.append(s[0:i])
            if n!=i*i:
                a.append(s[0:n//i])
    return a
def hai(s):
    a = uoc(s)
    n = len(s)
    for i in a:
        for j in range(0,n+1,a[i]):
            check = True
            if not a[i]==s[j:a[i]+1]:
                check = False   
                continue
            if check:
                return a[i]
n = int(input())
ss = []
for i in range(n):
    ip = input()
    ss.append(ip)
for i in ip: