import sys
#sys.stdin = open("muave.inp", "r")
#sys.stdout = open("muave.out", "w")

def khanh(n,k,a,b):
	if k == 1:
		a =b
	if n>k:
		return min((n%k)*a+(n//k)*b,(n//k+1)*b)
	else:
		if b<a*n:
			return b
		else:
			return a*n
n,k,a,b = map(int,input().split())
print(khanh(n,k,a,b))