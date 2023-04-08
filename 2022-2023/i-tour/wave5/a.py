from math import ceil


def divide(n, m):
    x = round(n / m)

    if x * m == n:
        return [(x, m)]

    other_amount = abs(n - x * m)
    return [(x, m - other_amount), (x - 1 if n < x * m else x + 1, other_amount)]


def get_portions(divided, k):
    return sum([ceil(dish[0] / k) * dish[1] for dish in divided])


n = int(input())  # количество зелюков
m = int(input())  # количество приемов пищи
k = int(input())  # размер порции зелюков, съедаемых за одну минуту

for i in range(n, n + 5):
    res = divide(i, m)
    print(i, "=", "".join([(str(x[0]) + " + ") * x[1] for x in res]))
    ans = get_portions(res, k)
    print(i, ans)
