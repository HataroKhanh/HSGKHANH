import re

chuoi_test = "aaabbbbc"
ket_qua_test = re.findall(r'((\w)\2*)', chuoi_test)
print(ket_qua_test)
