a = []
for i in range(3):
    a.append(int(input()))
print(sorted(a)[1] if a[0]!=a[1]!=a[2] else -1) 
