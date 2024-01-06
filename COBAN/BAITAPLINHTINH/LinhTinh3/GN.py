a,b,c,d = map(int,input().split())
print(abs(c-b if b>=c else a-d if a>=d else 0))
