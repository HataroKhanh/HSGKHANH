#!/bin/bash

# Lấy danh sách các file .cpp và .py chưa được theo dõi (untracked) từ git status
untracked_files=$(git status --porcelain | grep -E '^\?\? .*\.(cpp|py)$' | cut -c 4-)

# Lặp qua mỗi file untracked
for file in $untracked_files; do
    # Kiểm tra xem file có tồn tại không
    if [[ -f "$file" ]]; then
        # Add file vào git
        git add "$file"

        # Lấy tên file không bao gồm phần mở rộng để làm thông điệp commit
        filename=$(basename "$file" | sed 's/\(.*\)\..*/\1/')

        # Commit với thông điệp là tên file
        git commit -m "$filename"
    fi
done
git push