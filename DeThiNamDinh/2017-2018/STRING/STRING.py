s=input().split(' ')
a=[len(i) for i in s]
d=max(a)
n=len(s)
for i in range(n):
    if a[i]==d:
        print(s[i])
        break


