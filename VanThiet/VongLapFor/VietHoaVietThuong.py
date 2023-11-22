a=input()
h,t=0,0
for i in a:
    if i==i.lower():
        t+=1
    elif i==i.upper():h+=1
print(f"Viet Hoa: {h}\nViet Thuong: {t}")