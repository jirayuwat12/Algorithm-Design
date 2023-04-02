import sys
input = sys.stdin.readline

[n,e] = list(map(int, input().split()))

g = dict()
for i in range(1,n+1):
    g[i] = []

for _ in range(e):
    [u,v] = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

def DFS():
    ret =0
    visited = dict()
    for cd in range(1,n+1):
        if cd not in visited:
            ret += 1
        q = [cd]
        while len(q) != 0:
            temp = q.pop(0)
            visited[temp] = True
            for ch in g[temp]:
                if ch not in visited:
                    q.append(ch)
    return ret
print(DFS())