def uoc(s):
    n = len(s)
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            a.append(s[0:i])
            if n!=i*i:
                a.append(s[0:n//i])
    return a
def hai(s):
    a = uoc(s)
    n = len(s)
    b= []
    for i in a:
        if i*(n//len(i))==s:
            b.append(i) 
    return min(b)
n = int(input())
for i in range(n):
    print(hai(input()))