from math import ceil

n, m, k = [int(input()) for _ in range(3)]
print(ceil((n // m + 1) / k) * (n % m) + ceil((n // m) / k) * (m - n % m))
