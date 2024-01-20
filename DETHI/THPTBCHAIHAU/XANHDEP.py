import re
n = int(input())
smax = 0
for i in range(n):
    s = input()
    a = re.findall(r'((\w)\2*)', s)
    smax = max(smax,len(max(a)[0]))
print(smax)