
def countWays(N):
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

# Đọc từ file TILE.INP và ghi kết quả vào TILE.OUT
""" with open('TILE.INP', 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

with open('TILE.OUT', 'w') as file:
    for number in numbers:
        file.write(str(countWays(number)) + '\n') """
numbers=[2,8,12]
for i in numbers:
    print(countWays(i))
