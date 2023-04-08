from datetime import datetime


n, m = [int(input()) for _ in range(2)]

DATETIME_FORMAT = "%d.%m.%Y"

stations_data = {i: [] for i in range(1, n + 1)}
visits = {i: [] for i in range(1, n + 1)}

for i in range(m):
    cn, date = input().split()
    stations_data[int(cn)].append(datetime.strptime(date, DATETIME_FORMAT))


k = int(input())
for i in range(k):
    cn, date = input().split()
    visits[int(cn)].append(datetime.strptime(date, DATETIME_FORMAT))

map(lambda x: x.sort(), stations_data.values())

ans = 0
for cn in visits:
    if not visits[cn]:
        continue

    visits[cn].sort()

    for vdate in visits[cn]:
        if stations_data[cn] and vdate >= stations_data[cn][0]:
            stations_data[cn].pop(0)
            ans += 1

print(ans)
