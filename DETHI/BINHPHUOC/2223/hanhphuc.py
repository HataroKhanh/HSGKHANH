def nt(n):
    if n<=1:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n,k = map(int,input().split())
a = []
for i in range(k):
    l,r = map(int,input().split())
    check = False
    for j in a:
        if (l in j) or (r in j):
            j.add(r)
            j.add(l)
            check = True
    if not check:
        a.append({l,r})
def merge_sets(sets):
    merged_sets = []

    for current_set in sets:
        merged = False
        for merged_set in merged_sets:
            if current_set & merged_set:
                merged_set |= current_set
                merged = True
                break
        if not merged:
            merged_sets.append(current_set)

    return merged_sets

a = merge_sets(a)
b = []
for i in a:
    for j in i:
        b.append(j)
d = 0
for i in range(1,n+1):
    if i not in b:
        a.append({i})

for i in a:
    if not nt(len(i)):
        d+=1
print(d)
"""
30 18
10 11
8 24
12 17
21 28
10 21
23 30
10 22
17 24
7 23
22 28
17 18
6 28
20 24
21 25
28 29
8 19
23 30
15 26


11

"""