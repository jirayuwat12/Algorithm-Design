import sys
import heapq
sys.setrecursionlimit(100000)
input = sys.stdin.readline

[n, e] = list(map(int, input().split()))
color_map = [-1 for _ in range(n)]
g = dict()

for _ in range(e):
    [u, v] = list(map(int, input().split()))
    if u not in g:
        g[u] = dict()
    g[u][v] = -1
    if v not in g:
        g[v] = dict()
    g[v][u] = -1

'''
DFS and backtracking
'''
color_map = [-1 for i in range(n)]

ans = 1e10

q = [(1,0, list(color_map))]
while len(q):
    _, u, color_map = heapq.heappop(q)
    if len(list(set(color_map))) - (-1 in color_map) > ans:
        continue

    ncolor = set()
    if u in g:
        for v in g[u]:
            ncolor.add(color_map[v])

    for color in range(n):
        if color in ncolor:
            continue
        color_map[u] = color


        if -1 not in color_map:
            ans = min(ans,len(list(set(color_map))))
        else:
            for v in range(n):
                if color_map[v] == -1:
                    num_1 = 0
                    for k in color_map:
                        if k == -1:
                            num_1 += 1
                    if ans == 1e10:
                        heapq.heappush(q, (len(list(set(color_map))), v, list(color_map)))
                    break
print(ans)