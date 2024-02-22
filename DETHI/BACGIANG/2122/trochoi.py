n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))

i,j = 0,0
ssum = 0
while i<n and j<n:
	ssum  = abs(a[i]+b[j])
	if i!=n-1 and abs(a[i+1]+b[j])<ssum:
		i+=1
	elif j!=n-1 and abs(a[i]+b[j+1])<ssum:
		j+=1
	else:
		break
print(ssum)
