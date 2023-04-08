import itertools

check = [
    [1, 2, 0],
    [0, 1, 2],
    [2, 0, 1],
    [3, 4, 0],
    [3, 0, 4],
    [4, 0, 3]
]

found = False
for i in itertools.permutations(list(map(int, input().split()))):
    if all([i[j[0]] + i[j[1]] > i[j[2]] for j in check]):
        print(i[0])
        print(f"{i[1]} {i[2]}")
        print(f"{i[3]} {i[4]}")
        found = True
        break
if not found:
    print(0)
