l =[6,28,496,8128]
n = int(input())
a = [int(i) for i in input().split()]
d=0
for i in a:
    if sum([int(j) for j in str(i)]) in l:
        d+=1
print(d)        