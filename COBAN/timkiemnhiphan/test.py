max_range = int(10e5)  # Limiting the range to 10^5 for faster computation

for i in range(2, max_range + 1):
    d = 1  # Start from 1 as every number is divisible by 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            d += j
            if i // j != j:  # Avoid adding the square root twice
                d += i // j
    if d == i:
        print(i)
