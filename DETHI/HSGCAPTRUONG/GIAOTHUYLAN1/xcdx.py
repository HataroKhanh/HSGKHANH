def rev(s):
    return s == s[::-1]
def nmax(S):
    n = len(S)
    smax = 0
    for i in range(n):
        for j in range(i, n):
            s = S[i:j+1]
            if rev(s) and len(s) > smax:
                smax = len(s)
    return smax
S = input().strip()
r = nmax(S)
print(str(r))
