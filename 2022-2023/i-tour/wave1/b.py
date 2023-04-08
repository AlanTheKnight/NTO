n, k =  map(int, input().split())

f = list(range(2, n + 1, 2))
s = list(range(1, n + 1, 2))

if k % 2 == 0:
    even_direction = False if k == f[0] else True
    if even_direction:
        f.reverse()
    print(*f, end=" ")
    if not even_direction:
        s.reverse()
    print(*s, end=" ")
else:
    odd_direction = False if k == s[0] else True
    if odd_direction:
        s.reverse()
    print(*s, end=" ")
    if not odd_direction:
        f.reverse()
    print(*f, end=" ")
