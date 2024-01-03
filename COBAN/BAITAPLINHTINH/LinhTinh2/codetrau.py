def find_fastest_way(table, k):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == k:
                return f'{k} found at row {i+1}, column {j+1}'
    
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] * (j+1) == k:
                return f'{k} can be reached by row {(i+1)} and column {(j+1)}'
    
    return f'{k} cannot be reached in this table'

# Example table
table = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12]
]

# Example usage
number_to_find = 6
result = find_fastest_way(table, number_to_find)
print(result)

