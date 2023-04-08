h, m = map(int, input().split())

x = h * 60 + m

for i in range(10):
    print(x // 60, x % 60)
    x += 9
    if x > 24 * 60:
        x -= 24 * 60
