def count_ways(N, d, prices):
    prices.sort()
    count = 0
    for i in range(N):
        j = i + 2
        while j < N and prices[j] - prices[i] <= d:
            count += (j - i - 1)
            j+=1
    return count
N,d = map(int,input().split())
prices= [int(i) for i in input().split()]
result = count_ways(N, d, prices)
print(result)
