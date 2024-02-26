def dx(s):
    return s[::-1]

s = input()
n = len(s)
smax = 0
for i in range(n):
    for j in range(i,n):
        snew = s[i:j+1]
        if snew == dx(snew):
            smax = max(smax,len(snew))
print(smax)
