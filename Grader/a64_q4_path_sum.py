import sys
import heapq
input = sys.stdin.readline

g = dict()

[n, m] = list(map(int, input().split()))
k = list(map(int, input().split()))
for _ in range(m):
    [u, v, w] = list(map(int, input().split()))
    if u not in g:
        g[u] = dict()
    g[u][v] = w
    if v not in g:
        g[v] = dict()
    g[v][u] = w

possible = set()

def search(cnode, ki):
    global  possible
    q = [(0, cnode, set([cnode]))]
    while len(q):
        top = heapq.heappop(q)
        dist, current, visited = top
        possible.add(dist)
        visited = set(visited)
        if dist > ki:
            return False
        if dist == ki:
            return True
        if current in g:
            for v in g[current]:
                if v not in visited and dist + g[current][v] <= ki:
                    visited.add(v)
                    heapq.heappush(q, (dist + g[current][v], v, set(visited)))
                    visited.discard(v)

    return False

for node in range(n):
    search(node,max(k))

for i in range(8):
    ki = k[i]
    if ki in possible:
        print('YES')
    else:
        print('NO')