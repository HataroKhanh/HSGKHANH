
# Giả sử a = [8, 2, 4, -5, 9, 1, -3] từ ví dụ đề bài
a = [8, 2, 4, -5, 9, 1, -3]

# Tiến hành tìm giá trị lớn nhất của biểu thức a[i] + a[j] - a[k]
# def find_max_expression(a):
n = len(a)
X = [0] * n  # Mảng X[i] là max của đoạn từ A[1] tới A[i-1]
Y = [0] * n  # Mảng Y[i] là min của đoạn từ A[i+1] tới A[n]

# Xây dựng mảng X
X[0] = a[0]
for i in range(1, n):
    X[i] = max(X[i-1], a[i-1])

# Xây dựng mảng Y
Y[n-1] = a[n-1]
for i in range(n-2, -1, -1):
    Y[i] = min(Y[i+1], a[i+1])

# Tìm giá trị lớn nhất của biểu thức a[i] + a[j] - a[k]
max_value = max(a[i] + X[i] - Y[i] for i in range(1, n-1))

    # return max_value
print(X,Y,max_value)
# Gọi hàm và in kết quả
# print(find_max_expression(a))
