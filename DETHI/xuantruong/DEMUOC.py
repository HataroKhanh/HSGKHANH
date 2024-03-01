n = int(input())
c = 0
l = 0
for i in range(n):
    ip = int(input())
    if int(ip**0.5) == ip**0.5:
        l += 1
    else:
        c += 1
print(c)
print(l)
