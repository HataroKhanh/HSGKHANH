def count_pairs(n, arr):
    max_val = 10**9
    max_pow = 31
    
    pow2 = [2**i for i in range(max_pow)]
    
    count = 0
    freq_map = {}
    
    for i in range(n):
        for j in range(max_pow):
            target = pow2[j] - arr[i]
            if target in freq_map:
                count += freq_map[target]
        
        if arr[i] in freq_map:
            freq_map[arr[i]] += 1
        else:
            freq_map[arr[i]] = 1
    
    return count

# Đọc dữ liệu từ file DEMCS.INP
n = int(input().strip())
arr = list(map(int,input().split()))

# Gọi hàm và in kết quả
result = count_pairs(n, arr)
print(result)
