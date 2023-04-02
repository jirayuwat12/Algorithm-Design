import sys
input = sys.stdin.readline

[r, c, t] = list(map(int, input().split()))

g = []
q = []
ret = 0
for i in range(r):
    g.append(list(map(int, input().split())))
    for j in range(c):
        if g[i][j] == 1:
            q.append((0, i, j))
            g[i][j] = 0

while len(q) != 0 and q[0][0] <= t:
    d, i, j = q.pop(0)
    if g[i][j] == 1:
        continue
    ret +=1
    g[i][j] = 1
    d += 1
    if i-1 >= 0 and g[i-1][j] == 0:
        q.append((d, i-1, j))
    if i+1 < r and g[i+1][j] == 0:
        q.append((d, i+1, j))
    if j-1 >= 0 and g[i][j-1] == 0:
        q.append((d, i, j-1))
    if j+1 < c and g[i][j+1] == 0:
        q.append((d, i, j+1))

print(ret)
