def generate_combinations(s, current="", index=0):
    if index == len(s):
        if current:
            print(current)
        return

    # Thêm ký tự hiện tại vào chuỗi kết quả
    generate_combinations(s, current + s[index], index + 1)

    # Không thêm ký tự hiện tại vào chuỗi kết quả
    generate_combinations(s, current, index + 1)

# Sử dụng hàm với chuỗi đầu vào "1234"
s = input()
generate_combinations(s)
