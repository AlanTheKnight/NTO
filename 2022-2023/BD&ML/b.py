
from math import sqrt


def get_average(data):
    return sum(data[i][0] * data[i][1] for i in range(len(data))) / sum(map(lambda x: x[1], data))


def corrcoef2(x):
    avg_x = len(x) / N
    s_x = sqrt((1 / (N - 1)) * sum([((1 if i in x else 0) - avg_x) ** 2 for i in range(N)]))
    r = (1 / (N - 1)) * sum([
        (((1 if i in x else 0) - avg_x) / s_x) * ((b[i] - avg_y) / s_y) for i in range(N)
    ])
    return r


N, K = 6, 3

a = list(map(int, "1 2 2 3 3 3".split()))
b = list(map(int, "1 2 3 4 5 6".split()))

avg_y = sum(b) / N
s_y = sqrt((1 / (N - 1)) * sum([(i - avg_y) ** 2 for i in b]))

data = []

categories = {}
for i in range(N):
    if a[i] not in categories:
        categories[a[i]] = set()
    categories[a[i]].add(i)

for c in categories:
    x = categories[c]
    data.append((corrcoef2(x), len(x)))

# print(data)
get_average(data)
