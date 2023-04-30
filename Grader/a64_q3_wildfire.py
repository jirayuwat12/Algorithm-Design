import sys
input = sys.stdin.readline

[V,E,k] = list(map(int, input().split()))
b = list(map(int, input().split()))
all_b = sum(b)
starts = list(map(int, input().split()))
g = dict()
for i in range(V):
    g[i] = dict()
for _ in range(E):
    [u,v] = list(map(int, input().split()))
    g[u][v] = 1

__visited = dict()
for start in starts:
    q = [start]
    while len(q):
        u = q.pop(0)
        if u not in __visited:
            __visited[u] = 0
            all_b -= b[u]
            for v in g[u]:
                q.append(v)
    print(all_b,end = ' ')
