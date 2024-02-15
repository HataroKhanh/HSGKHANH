a,b = map(int,input().split())

n = (b-a+1)*(a+b)/2
d = 0
for i in range(a,b+1):
	if i%13==0:
		d+=i
print(int(n-d))
