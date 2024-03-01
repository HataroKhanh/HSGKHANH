from collections import defaultdict
import sys

n = int(input())
s = input()

f = defaultdict(lambda: 0)
for i in s:
    f[i] += 1

i, j = 1, 3
s = "t" + s + s

if n & 1 == 1:
    print(-1)
    sys.exit(0)

while i <= n:
    fnew = defaultdict(lambda: 0)

    ns = s[i : j + 1]

    for d in ns:
        fnew[d] += 1

    if (
        fnew["T"] != 0
        and fnew["S"] != 0
        and f["S"] / 2 == fnew["S"]
        and f["T"] / 2 == fnew["T"]
    ):
        if j > n:
            print(i, j - n)
        else:
            print(i, j)
    i += 1
    j += 1
