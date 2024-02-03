s = input()
n = int(input())

smax = max(map(int, s[:len(s)-n+1]))
start_index = s.find(str(smax))
n -= start_index
s = s[start_index:]
i = 0
while n > 0:
    try:
        if s[i] == str(min(map(int, s))):
            s = s[:i] + s[i+1:]
            n -= 1
        else:
            i += 1
    except:break
print(s)
