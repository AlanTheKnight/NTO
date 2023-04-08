INF = 10 ** 10


def get_table(a):
    money = list(sorted([i for i in range(a, 2 * a + 1)], reverse=True))
    # money = [i for i in range(a, 2 * a + 1)]
    M = sum(money)
    arr = [INF] * (M + 1)
    prev = {}
    arr[0] = 0
    for c in money:
        for k in range(M , -1, -1):
            if k - c >= 0 and arr[k - c] + 1 < arr[k]:
                arr[k] = arr[k - c] + 1
                if k not in prev:
                    prev[k] = k - c
    return arr, prev


def get_ans(b, prev):
    ans = []
    cur = b
    while prev[cur] != 0:
        ans.append(cur - prev[cur])
        cur = prev[cur]
    ans.append(cur)
    ans.sort()
    return ans


def solve(a, b):
    arr, prev = get_table(a)
    for index, value in enumerate(arr):
        if index and value != INF:
            ans = get_ans(index, prev)
            print(index, ans, len(ans), value)
            # assert len(ans) == arr[index]

a, b = map(int, input().split())
solve(a, b)
