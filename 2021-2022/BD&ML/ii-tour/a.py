from copy import deepcopy


n, m = map(int, input().split())
f, s = [], []
for i in range(n):
    f.append(list(map(int, input().split())))
for i in range(n):
    s.append(list(map(int, input().split())))


for selected in range(n):
    cur1 = f[selected]
    changed = {el: s[0][i] for i, el in enumerate(cur1)}

    g = [[None for i in range(m)] for j in range(n)]
    
    for row in range(n):
        for col in range(m):
            g[row][col] = changed[f[row][col]]
    
    search_deepcopy = deepcopy(s)
    result = []
    failture = False
    for i in g:
        try:
            pos = search_deepcopy.index(i)
            search_deepcopy[pos] = None
            result.append(pos + 1)
        except:
            failture = True
    
    if failture:
        continue

    print("YES")
    print(*result)

    # Выводим список замен
    replacement = []
    for i in range(1, m + 1):
        replacement.append(changed[i])
    print(*replacement)

    exit(0)

print("NO")
