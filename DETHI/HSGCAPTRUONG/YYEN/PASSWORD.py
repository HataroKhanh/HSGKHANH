def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def maxs(T):
    maxp = 0

    for i in range(len(T)):
        t = ""
        for j in range(i, len(T)):
            if T[j].isdigit():
                t += T[j]
                if t != "0" and is_prime(int(t)):
                    maxp = max(maxp, int(t))
    return maxp
T = input().strip()
result = maxs(T)
print(str(result))
