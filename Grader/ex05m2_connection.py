import sys
input = sys.stdin.readline

[n,e,k] = list(map(int, input().split()))

g = dict()
for i in range(n):
    g[i] = list()

def count_k(node):
    ret = 0
    q = [(0,node)]
    visited = dict()
    while(len(q) != 0):
        d,n = q.pop(0)
        visited[n] =True
        if d == k:
            ret += 1
            continue
        for ch in g[n]:
            if ch not in visited:
                q.append((d+1,ch))
    return ret

for _ in range(e):
    [u,v] = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
ret = -1
for i in range(n):
    ret = max(ret,count_k(i))
print(ret)