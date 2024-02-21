from math import ceil

def khanh(T,K,A,N):
	water_in_tank = 0
	for i in range(N):
		water_flow_in = min(K, A[i] - water_in_tank)
		water_in_tank += water_flow_in
		if water_in_tank == A[i]: 
			water_in_tank = 0
	return water_in_tank == 0
n , k = map(int,input().split())
a = list(map(int,input().split()))
i=0;j=0
for r in a:
	j = max(j,ceil(r/k))
mid = 0
print(i,j)
while i<=j:
	mid = (i+j)//2
	td = khanh(mid,k,a,n)
	if td:
		j=mid-1
	else:
		i=mid+1 
	print(i,j)
print(mid)
