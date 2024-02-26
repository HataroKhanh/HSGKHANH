def cp(n):
    return int(n**0.5)==n**0.5 and n!=0

n = input()
print(int(cp(sum(map(int,n)))),len(n),end = ' ')