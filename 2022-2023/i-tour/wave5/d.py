def get_min_dist(a, b):
    return min(len(s) - max(a, b) - 1 + min(a, b), max(a, b) - min(a, b) - 1)


def get_dist(a, b):
    r = b > a
    x = max(a, b)
    y = min(a, b)
    d1 = len(s) - x - 1 + y
    d2 = x - y - 1
    return (d1, d2) if r else (d2, d1)


s = input()

chips = [i for i in range(len(s)) if s[i] == "*"]

print(chips)

best_pos = 10**9
best_chip = -1

for c in chips:
    rs = 0
    for x in chips:
        if x != c:
            rs += get_min_dist(c, x)
    if rs < best_pos:
        best_pos = rs
        best_chip = c

left = [(get_min_dist(i, best_chip), i) for i in chips if i != best_chip]

left.sort()

cur = [best_chip, best_chip]

ans = 0

for dist, chip in left:
    dlb = get_dist(cur[0], chip)[1]
    drb = get_dist(cur[1], chip)[0]

    if drb < dlb:
        # print(chip, "Right side", drb)
        ans += drb
        cur[1] -= 1
    else:
        # print(chip, "Left side", dlb)
        cur[0] += 1
        ans += dlb

print(ans)
