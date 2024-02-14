def tach_chuoi(s):
    kq = []
    n = len(s)

    for i in range(1, n + 1):
        for j in range(n - i + 1):
            kq.append(s[j:j+i])
    return kq
def tach_so(s):
    kq = []
    n = len(s)
    t = ''
    for i in s:
        if i.isnumeric():
            t+=i
        else:
            if t!='':
                kq.append(t)
                t=''
    if t!='':
        kq.append(t)
    return kq
def nt(s):
    n = int(s)
    if n<=1:return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

s = input()
dmax = -1
tachso = tach_so(s)
for i in tachso:
    k = tach_chuoi(i)
    for j in k:
        if nt(j):
            dmax = max(dmax,int(j))
print(dmax)

