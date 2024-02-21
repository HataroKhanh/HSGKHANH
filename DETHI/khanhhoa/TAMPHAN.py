def khanh(n):
	if n==1:
		return ['0','1','2']
	else:
		a=[]
		d = khanh(n-1)
		for i in d:
			a.append(i+'0')
			if i[-1]!='1':
				a.append(i+'1')
			a.append(i+'2')
		return a
print(khanh(int(input())))