def khanh(s):
	return s[::-1]==s

s = input().split()
d = 0
for i in s:
	if khanh(i):
		d+=1
print(d)