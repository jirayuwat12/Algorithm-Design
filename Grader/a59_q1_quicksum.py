import sys
input = sys.stdin.readline

[n, m, k] = [int(x) for x in input().split()]

a = []

for _ in range(n):
    a.append([int(x) for x in input().split()])
    for i in range(1, m):
        a[-1][i] += a[-1][i-1]

for i in range(1, n):
    for j in range(m):
        a[i][j] += a[i-1][j]

for _ in range(k):
    [r1, c1, r2, c2] = [int(x) for x in input().split()]
    s = a[r2][c2]
    if r1-1 >= 0:
        s -= a[r1-1][c2]
    if c1-1 >= 0:
        s -= a[r2][c1-1]
    if r1-1 >= 0 and c1-1 >= 0:
        s += a[r1-1][c1-1]
    print(s)
