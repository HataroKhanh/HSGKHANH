
a, b, c = map(int, input().split())
x = 0
i = a
while i <= b:
    x = x+1 if (i >= a and i <= b and i % c != 0) else x
    i += 1
print(x)

