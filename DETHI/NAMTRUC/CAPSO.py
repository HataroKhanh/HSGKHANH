def khanh(a, b):
    if a >> 1 == b or b >> 1 == a:
        return "1"
    else:
        d = 0
        a = bin(a)[2:]
        b = bin(b)[2:]
        for i in range(len(b)):
            if a[i] != b[i]:
                d += 1
            if d > 1:
                return "0"
        return "1"


t = ""
while 1:
    try:
        a, b = map(int, input().split())
        t += khanh(a, b)
    except:
        print(t)
        break
