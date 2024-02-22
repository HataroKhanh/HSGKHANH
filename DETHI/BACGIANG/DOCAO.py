#code trau
def trau(n,m):
	i=10
	a = []
	while i<=n:
		if nt(i) and sum(map(int,str(i)))==m:
			a.append(i)
		i+=1
	return a

def san():
    a = [1] * int(10e6)
    a[0] = a[1] = 0
    for i in range(2, int(int(10e6)**0.5) + 1):
        if a[i] == 1:
            for j in range(i*i, int(10e6), i):
                a[j] = 0
    return a

def nt(n):
	if n<=1:return False
	for i in range(2,int(n**0.5)+1):
		if n%i==0:return False
	return True

n = int(input())
m = int(input())
a = san()
sdem = 0
for i in range(10,n+1):
	if a[i]==1 and sum(map(int,str(i)))==m:
		print(i)
		sdem+=1
print(sdem)