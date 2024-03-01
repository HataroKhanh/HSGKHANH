from math import comb

n, m = map(int, input().split())
d = 0
d += comb(6, 2) * comb(n, 2)
d += comb(6, 2) * comb(m, 2)
d += comb(6, 2) * (comb(m, 1) * comb(n, 1))
print(d)
