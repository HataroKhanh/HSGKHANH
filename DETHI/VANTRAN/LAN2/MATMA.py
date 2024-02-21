n = input()
if '0' in n and sum(map(int,n))%3==0:
	print(''.join(sorted(n, key = lambda x : int(x), reverse=True)))
else:print(-1)