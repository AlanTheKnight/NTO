x = int(input())
p = 0

ops = []

while p < x or abs(p - x) % 2 != 0:
    p += 3
    ops.append("3")
    if p == x:
        break

# print(p)

while p != x:
    p -= 2
    ops.append("-2")

print(len(ops))
print(*ops)
