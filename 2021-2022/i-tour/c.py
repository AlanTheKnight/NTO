m = {}
a = int(input())

for i in range(a-1):
    f, s = input().split(' ')
    m[f] = s
    if s not in m:
        m[s] = False

first = None
for i in m.items():
    if not i[1]:
        first = i[1]

for count in range(a):
    for i in m.items():
        if i[1] == first:
            print(i[0])
            first = i[0]
            break