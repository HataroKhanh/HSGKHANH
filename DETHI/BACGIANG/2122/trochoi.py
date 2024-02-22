n = int(input())
a = [0]+sorted(list(map(int,input().split())))
b = [0] +sorted(list(map(int,input().split())))
i,j = 1,n
ssum = float('inf')
while i<=n and j>0:
	ssum  = min(abs(a[i]+b[j]),ssum)
	if ssum == 0:break
	if (a[i]+b[j]>0):
		j-=1
	else:
		i+=1
print(ssum)
