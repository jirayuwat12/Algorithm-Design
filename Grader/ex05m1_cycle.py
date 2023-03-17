import sys
input = sys.stdin.readline

def add_edge(g:dict, u,v):
    if u in g:
        g[u].append(v)
    else:
        g[u] = [v]

def detect_cycle(g):
    visited = set()
    for u in g:
        if u not in visited:
            q = list()
            q.append([u,None])
            while len(q) != 0 :
                [cn,ln] = q[0]
                q = q[1:]
                visited.add(cn)
                for v in g[cn]:
                    if v == ln:
                        continue
                    if v in visited:
                        return True
                    else:
                        q.append([v,cn])
    return False

t = int(input())
for _ in range(t):
    [n,e] = list(map(int, input().split()))
    g = dict()
    for _ in range(e):
        [u,v] = list(map(int, input().split()))
        add_edge(g,u,v)
        add_edge(g,v,u)
    if e > n-1:
        print('YES')
        continue
    print(['NO','YES'][detect_cycle(g)])
