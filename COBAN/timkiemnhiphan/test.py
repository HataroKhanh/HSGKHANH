def khanh(a,n,k,m):
    d = 0
    s = 0
    v = m*2
    check = True
    for i in a:
        if check:
            v = i+m*2
            check = False
        if i==v:
            d+=1
            check = True
        elif i>v:
            i-=1
            d+=1
            check = True
    print(d)
print(khanh([1,2,3,4,5],5,2,3))