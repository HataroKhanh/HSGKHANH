n , k = map(int,input().split())
a = list(map(int,input().split()))
i=0
j=0
sum=0
d=0
while j<n:
    sum+=a[j]
    while i<n and sum>k:
        sum-=a[i]
        i+=1
    d+=j-i+1
    j+=1
print(d)

