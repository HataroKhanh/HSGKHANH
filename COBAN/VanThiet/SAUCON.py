n = int(input())
s = input()[:n]
a=['a','e','i','o','u']
i,j,dem=0,0,0

while (j<n):
    if (s[j] in a) and i<j:
        i+=1
    else:
        dem=max(dem,j-i)
        j+=1
print(dem)
    
