a,b = map(int,input().split())
if a<=12 and b<=12:
    if b-a>4:
        print(4*6+(b-a)*3)
    else:
        print((b-a)*6)
elif a>=12 and b>=12:
    if b-a>=4:
        print(4*10+(b-a-4)*5)
    else:
        print((b-a)*10)
else:
    t = 12-a
    s = b-12
    if t>=4:
        print((4)*4+(b-a-4)*5)
    elif t<4 and b>=(4-t):
        print(t*6+(4-t)*10+(b-4-t)*5)
    else:
        print(t*6+s*10)
    
    
    
