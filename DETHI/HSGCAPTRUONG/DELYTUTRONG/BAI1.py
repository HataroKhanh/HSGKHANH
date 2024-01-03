l = ['u','e','o','a','i']
n = int(input())
d=0
a = input()
for i in a:
    if i in l:
        d+=1
print(n-d-1)
