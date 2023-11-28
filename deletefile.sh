#!/bin/bash

# Xác định thư mục chứa script
DIRECTORY=$(dirname "$0")

# Xác định tên file script
SCRIPT_NAME=$(basename "$0")

# Thay đổi thư mục làm việc hiện tại thành thư mục chứa script
cd "$DIRECTORY" || exit

# Xóa các file đối tượng .o, trừ các file trong thư mục .git
find . -type f -name "*.o" ! -path "./.git/*" -exec rm {} +

# Xóa các file thực thi không có đuôi mở rộng, trừ file script và các file trong thư mục .git
find . -type f -executable ! -name "$SCRIPT_NAME" ! -path "./.git/*" -exec rm {} +
