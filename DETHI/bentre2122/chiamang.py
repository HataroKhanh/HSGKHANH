n = int(input())
a = list(map(int,input().split()))


for i in range(n):
    if sum(a[:i]) == sum(a[i:]):
        print(i)
        break
    

"""
5
2 2 3 6 1
"""