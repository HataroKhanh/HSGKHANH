import re

n = int(input())
s = input()
a = re.findall(r'(?=(\w+))', s)
b = 0
for i in a:
    if s.count(i)>=2:
        b = max(b,len(i))
print(b+1)
