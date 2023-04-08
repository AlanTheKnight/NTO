alpha = float(input())
h, m = map(int, input().split())

h_move = (30 * (h + m / 60))
m_move = (6 * (h * 60 + m))

print(h_move)
print(m_move)

delta = alpha - abs(m_move % 360 - h_move % 360)

if delta > 0:
    print(delta)
else:
    print(360 - abs(delta))
