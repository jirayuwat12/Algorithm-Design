import sys
input = sys.stdin.readline

n = int(input())
edge_list = []
for u in range(n-1):
    costs = list(map(int, input().split()))
    for v, cost in enumerate(costs):
        v = u + v + 1
        edge_list.append((cost, u, v))

edge_list = sorted(edge_list)


def mst():
    __parent = []
    __rank = []
    for i in range(n):
        __parent.append(i)
        __rank.append(0)

    e = 0
    ret = 0
    for edge in edge_list:
        if e == n-1:
            break
        else:
            w, u, v = edge
            ancu = __parent[u]
            while ancu != __parent[ancu]:
                ancu = __parent[ancu]
            ancv = __parent[v]
            while ancv != __parent[ancv]:
                ancv = __parent[ancv]
            if ancv != ancu:
                ret += w
                # union
                if __rank[ancu] > __rank[ancv]:
                    __parent[ancv] = ancu
                elif __rank[ancv] > __rank[ancu]:
                    __parent[ancu] = ancv
                else:
                    __parent[ancu] = ancv
                    __rank[ancv] += 1
                e += 1
    return ret


print(mst())
