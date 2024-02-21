def congpha(n):
	dem = 0
	for i in range(1,int(n**0.5)+1):
		if n%i==0:
			dem+=1
			if n!=i*i:
				dem+=1
	return dem*n

n = int(input())
a = list(map(int,input().split()))
result = 0
for i in a:
	result+=congpha(i)
print(result)