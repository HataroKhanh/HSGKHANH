def khnah(n):
    if n==3:return 1
    elif n==5:return 1
    elif n==1:return 1
    elif n<=0:return 1
    else:
        return min(khnah(n-3)+khnah(n),min(khnah(n-5)+khnah(n),khnah(n-1)+khnah(n)))
print(khnah(11))
