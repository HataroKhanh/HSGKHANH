"""
a+aa+aaa+aaaa
"""
a=input()
s=0
for i in range(1,5):
    s+=int(a*i)
    print(a*i)
