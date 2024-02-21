def khanh(a, idx, k):
    sleft = 0
    sright = 0
    temp = k
    for i in a:
        if i[0] > idx and temp != 0 and i[2] != 0:
            sright += i[1]
            temp -= 1
    temp = k
    for i in a:
        if i[0] < idx and temp != 0 and i[2] != 0:
            sleft += i[1]
            temp -= 1
    return sright >= sleft


def next_i(a, x, n):
    for i, j in enumerate(a):
        if j[0] > x and j[2] != 0:
            return i
    return n - 1


def back_i(a, x, n):
    for i in range(n - 1, -1, -1):
        if a[i][0] < x and a[i][2] != 0:
            return i
    return 0


f = []
n, x, k = map(int, input().split())

for i in range(n):
    a, b = map(int, input().split())
    f.append([a, b, 1])

a = sorted(f, key=lambda x: x[1])
ssum = 0
temp = x
while k >= 0:
    if khanh(a, x, k):
        x = next_i(a, x, n)
        if k>=x-temp:
	        a[x][2] = 0
	        ssum += a[x][1]
	        k -= x - temp
        else:
            break
    else:
        x = back_i(a, x, n)
        if k>=x-temp:
	        a[x][2] = 0
	        ssum += a[x][1]
	        k -= temp - x
        else:break
    temp = x
    print(k)

print(ssum)
