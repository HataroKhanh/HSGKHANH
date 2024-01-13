from collections import defaultdict
def thiet(n):
	f=defaultdict(lambda :0)
	fmin='0'
	for i in n:
		f[i]+=1
	for i in f.items():
		if i[1]==1:
			fmin=i[0]
	return n.find(fmin)+1 if fmin!='0' else -1
n=int(input())
for i in range(n):
	k=input()
	print(thiet(k))


