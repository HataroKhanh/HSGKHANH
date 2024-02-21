n = int(input())
f0 = 0
f1 = 1
mod =int(1e9)+7
for i in range(n):
	f = ((f0%mod)+(f1%mod))%mod
	f0,f1 = f,f0
print(f)