from sklearn.linear_model import LinearRegression
from math import pi, sin, cos, floor
import random


DEBUG = False
r = LinearRegression()

mi = [12, 24, 168, 672]


def get_data(i):
    d = []
    for j in range(4):
        d.extend([
            cos(i/mi[j] * 2 * pi) * cos(pi / 12),
            sin(i/mi[j] * 2 * pi) * sin(pi / 12),
        ])
    return d


if DEBUG:
    ans = [random.randint(1, 1000) for i in range(int(168/6))]
    ans = ans*6
    for i in range(random.randint(30, 84)):
        ans[random.randint(0, 167)] = random.randint(1, 1000)
else:
    ans = []

inp = []

for i in range(168):
    if not DEBUG:
        ans.append(int(input()))
    inp.append(get_data(i))

r.fit(inp, ans)

inp = []
for i in range(168, 336):
    inp.append(get_data(i))

q = r.predict(inp)
for i in q:
    print(floor(i))
