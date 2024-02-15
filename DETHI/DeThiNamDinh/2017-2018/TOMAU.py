from collections import defaultdict
import sys
def DEMSO(s):
    X = 0
    D = 0
    V = 0
    k = defaultdict(int)
    for i in s:
        if i == 'V':
            k['V'] += 1
        elif i == 'D':
            k['D'] += 1
        elif i == 'X':
            k['X'] += 1
    return k
def TOMAU(s, k):
    return min(k['V']+k['X']*2,min(k['D']+k['V']*2,k['X']+k['D']*2)) 
#VVVVDDDDDVDDVXXVVDDXVVDXVVXDDVD
n = int(input())
a=[]
for i in range(n):
    s=input()
    k=DEMSO(s)
    a.append(str(TOMAU(s,k)))
print('\n'.join(a))
