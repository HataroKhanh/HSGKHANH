def nt(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def snt(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return nt(digit_sum)
def dp(l, r):
    kq = [num for num in range(l, r + 1) if nt(num) and snt(num)]
    return kq
l, r = map(int, input().split())
kq_list = dp(l, r)
print(' '.join(map(str, kq_list)))
