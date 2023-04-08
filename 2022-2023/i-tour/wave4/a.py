def solve(n):
    return 45 * (n // 10) + sum(list(range(10))[:(n % 10)])

print(solve(int(input())))
