def khanh(ip):
    s=''
    for i in ip:
        if i=='0':
            s+='5'
        else:
            s+=i
    return s
n = int(input())
for i in range(n):
    ip = input()
    print(khanh(ip))
