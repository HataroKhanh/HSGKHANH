l = ['u','e','o','a','i'] + [str(i) for i in range(0,10)]

n = int(input())
d=0
a = input()
for i in a:
    if  (i not in l):
        d+=1
print(d)
