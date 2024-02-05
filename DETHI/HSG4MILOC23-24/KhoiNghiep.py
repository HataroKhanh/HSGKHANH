n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())) + [i + 1])
a.sort()
l, r = 0, 0
index = 0
while a!=[]:
    lmin = min(a, key=lambda x: x[0])
    if lmin[0] <= l:
        l += 1
        a.remove(lmin)
    else:
        rmin = min(a, key=lambda x: min(x[0], x[1]))
        r += rmin[1]	
        l+=1
        a.remove(rmin)
print(r)
