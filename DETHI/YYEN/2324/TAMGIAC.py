from math import acos,degrees

a,b,c = map(int,input().split())

if a<b+c and b<a+c and c<a+b:
    ac,bc,cc = degrees(acos((b**2+c**2-a**2)/(2*b*c))),degrees(acos((a**2+c**2-b**2)/(2*a*c))),degrees(acos((b**2+a**2-c**2)/(2*b*a)))
    if 0<ac<=90 and 0<bc<=90 and 0<cc<=90:
        print(0)
    else:
        print(1)
else:
    print(0)
