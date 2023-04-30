import sys
input = sys.stdin.readline

[n,e,k] = list(map(int, input().split()))
g = dict()
for i in range(n+1):
    g[i] = list()

for _ in range(e):
    [u,v] = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

def BFS():
    visited = dict()
    visited[0] = 1
    q = [(0,0)]
    ret = 0
    while len(q):
        d,u = q.pop(0)
        if d == k :
            ret +=1
            continue
        d+=1
        for v in g[u]:
            if v not in visited:
                visited[v] = 1
                q.append((d,v))
    return ret

print(BFS())