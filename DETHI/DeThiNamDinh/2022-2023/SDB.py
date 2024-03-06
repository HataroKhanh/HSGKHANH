from math import ceil
def nt(n):
  if n<=1:return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True
n = int(input())
a = list(map(int,input().split()))

for i in a:
  t = ceil(i**0.5)
  while 1:
    if nt(t):
      print(t**2,end= ' ')
      break
    else:
      t+=1


