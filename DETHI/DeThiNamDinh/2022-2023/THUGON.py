import re
import sys
def f(s):
    if s =='':
        sys.exit(0)
    a = re.findall(r'((\w)\2*)', s)
    t = ''

    for i in a:
        if len(i[0])!=1:
            t+=str(len(i[0]))+i[1]
        else:
            t+=i[0]
    return t
while 1:
    try:
        print(f(input()))
    except Exception as e:
        break
