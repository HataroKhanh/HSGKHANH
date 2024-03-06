from math import ceil

n = int(input())
a = list(map(int,input().split()))
print(ceil(sum(a)/4))
