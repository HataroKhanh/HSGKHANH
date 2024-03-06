def count_triangles(arr):
    n = len(arr)
    arr.sort()
    count_acute, count_right, count_obtuse = 0, 0, 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            x, y = arr[i], arr[j]

            # Find the index of the largest side (k) that satisfies the triangle inequality
            k = binary_search(arr, j + 1, n - 1, x + y)

            # Count triangles based on their properties
            count_acute += k - j - 1
            count_right += 1 if x**2 + y**2 == arr[k]**2 else 0
            count_obtuse += n - k - 1

    return count_acute, count_right, count_obtuse

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Input
n = int(input())
que_lengths = list(map(int, input().split()))

# Count triangles
result = count_triangles(que_lengths)

# Output the results
print("Tam giac nhon:", result[0])
print("Tam giac vuong:", result[1])
print("Tam giac tu:", result[2])
