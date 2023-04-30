import sys
input = sys.stdin.readline

def stp(edge_list,V,start):
    dist = [1e10 for _ in range(V)]
    dist[start] = 0
    ck = False
    for _ in range(V-1):
        ck = False
        for edge in edge_list:
            u,v,w = edge
            if (dist[v] > dist[u] + w and dist[u] != 1e10):
                dist[v] = dist[u] + w
                ck = True
        if not ck:
            break
    return dist

[V,e,k] = list(map(int, input().split()))
start = int(input())
targets = list(map(int, input().split()))
edge_list = []
for _ in range(e):
    [u,v,w] = list(map(int, input().split()))
    edge_list.append((v,u,w))

l = stp(edge_list,V,start)
minn = 1e10
for target in targets:
    minn = min(minn,l[target])
print(minn)