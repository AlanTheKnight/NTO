h, w = map(int, input().split())
x = []
for row in range(h):
    x.append(input())

# print(x)

cnt = 0
for row in range(h):
    for col in range(w):
        if x[row][col] in ("/", "\\"):
            for i in range(4):
                dx = [1, -1, 0, 0]
                dy = [0, 0, -1, 1]
                if 0 <= row + dy[i] < h and 0 <= col + dx[i] < w and x[row+dy[i]][col+dx[i]] not in (".", x[row][col]):
                    cnt += 1

print(cnt // 2)
