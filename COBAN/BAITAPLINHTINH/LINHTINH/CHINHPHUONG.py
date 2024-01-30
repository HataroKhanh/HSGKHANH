def find_numbers():
    target_sum = 56

    for a in range(1, target_sum + 1):
        for b in range(a, target_sum + 1):
            for c in range(b, target_sum + 1):
                for d in range(c, target_sum + 1):
                    if a**2 + b**2 + c**2 + d**2 == target_sum:
                        return a, b, c, d

    return None

result = find_numbers()
if result:
    print("Các số nguyên dương a, b, c, d thỏa mãn:")
    print(result)
else:
    print("Không có giải pháp nguyên cho phương trình.")
