import math


def khanh(a, b):
    d = 0
    for i in range(a, b + 1):
        if math.gcd(i, int(str(i)[::-1])) == 1:
            d += 1
    return d


while 1:
    try:
        a, b = map(int, input().split())
        print(khanh(a, b))
    except:
        break
