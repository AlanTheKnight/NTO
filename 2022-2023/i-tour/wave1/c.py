n = int(input())

t = n * (n - 1) // 2

m = {}

for i in range(0, t):
    s = input()
    
    a, sign, b = s[0], s[1], s[2]
    
    if a not in m:
        m[a] = 0
    
    if b not in m:
        m[b] = 0

    if sign == ">":
        m[a] += 1
    else:
        m[b] += 1

print("".join([i[0] for i in sorted(list(m.items()), key=lambda x: x[1])]))
