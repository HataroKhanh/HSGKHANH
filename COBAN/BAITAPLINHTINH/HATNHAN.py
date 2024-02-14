'abababab'
import sys
def uoc(s):
    n = len(s)
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            a.append(i)
            if i*i!=n:
                a.append(n//i)
    return sorted(a)
def schar(s):
    a = uoc(s)
    b = []
    n = len(s)
    for i in a:
        if (s[:i]*(n//i))==s:
            return s[:i]
sys.stdin = open("HATNHAN.INP","r")
sys.stdout = open("HATNHAN.OUT", "w")
n = int(input())
for i in range(n):
    ip = input()
    print(schar(ip))
