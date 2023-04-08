def solve(a):
    for i in range(len(a)):
        r = 0
        for j in range(len(a) - i):
            r += a[j] * a[i + j]
        print(r, end=" ")
    print()

n = int(input())

a = list(map(int, input().split()))

solve(a)
