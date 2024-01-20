def tui(n):
    d = n // 5
    du = n % 5
    ba=0
    if du == 0:
        ba = 0
    elif du % 3 == 0:
        ba = du // 3
    else:
        d -= 1
        ba = (du + 5) // 3
    return d+ba
n = int(input())
print(tui(n))

