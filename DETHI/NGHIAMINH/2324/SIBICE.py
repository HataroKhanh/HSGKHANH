n,a,b = map(int,input().split())
k = (a**2+b**2)**0.5
for i in range(n):
    ip = int(input())
    print("DA" if k>=ip else "NA")