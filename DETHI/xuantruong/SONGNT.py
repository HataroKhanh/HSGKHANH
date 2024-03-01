def nt(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def check(s):
    return nt(s) and nt(sum(list(map(int, str(s)))))


while 1:
    try:
	    ip = int(input())
	    print("YES" if check(ip) else "NO")
	except:
   		break
