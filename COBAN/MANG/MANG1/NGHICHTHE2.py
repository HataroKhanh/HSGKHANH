def count_inversions(arr):
    n = len(arr)
    inversions = [0] * n

    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
        inversions[i] = count

    return inversions

def inversion_array(arr):
    inversions = count_inversions(arr)
    result = [0] * len(arr)

    for i in range(len(arr)):
        result[arr[i] - 1] = inversions[i]

    return result

# Ví dụ sử dụng:
n = 6
permutation = [4,3, 6, 2, 1, 5]

inversion_array_result = inversion_array(permutation)
print("Mảng nghịch thế:", inversion_array_result)
