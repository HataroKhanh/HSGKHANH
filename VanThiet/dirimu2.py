"""
{'1':1}
{'1':1,'2':4,'3':9,'4':16,'5':25}
Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) 
như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
"""
n=int(input())
a={}
for i in range(1,n+1):
    a[f'{i}']=i*i
print(a)