a = ['a', 'g', 'h']
b = "ag"

# Kiểm tra từng phần tử trong list a
all_exist = any(elem in b for elem in a)

# In kết quả
print(all_exist)

