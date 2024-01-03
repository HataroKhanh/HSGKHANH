n,m=map(int,input().split())
print(10//m if n==1 else (10**(n)-10**(n-1))//m)