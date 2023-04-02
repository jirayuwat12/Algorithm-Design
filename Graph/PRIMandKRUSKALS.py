import graph

g = graph.get_connected_graph(5, 0.6, weighted=True)


def kruskals(graph):
    __parent = dict()
    __rank = dict()
    for i in graph:
        __parent[i] = i
        __rank[i] = 0
    ret = dict()
    for i in graph:
        ret[i] = []

    # adj list -> edge sort
    edge_list = []
    for u in graph:
        for v in graph[u]:
            v, w = v
            edge_list.append((w, u, v))

    edge_list = sorted(edge_list)
    print(edge_list[:5])
    # select n-1 edges with not the same parent

    for _ in range(len(graph) - 2):
        i = 0
        while True:
            w, u, v = edge_list[i]
            pru = __parent[u]
            while pru != __parent[pru]:
                pru = __parent[pru]
            prv = __parent[v]
            while prv != __parent[prv]:
                prv = __parent[prv]

            if pru == prv:
                i += 1
            else:
                ret[u].append((v, w))
                # union parent u and v
                if __rank[pru] > __rank[prv]:
                    __parent[prv] = pru
                elif __rank[prv] > __rank[pru]:
                    __parent[pru] = prv
                else:
                    __parent[pru] = prv
                    __rank[prv] += 1
                break
        edge_list = edge_list[i+1:]
    return ret


if __name__ == '__main__':
    g = dict()
    for i in range(8):
        g[i] = []
    inp = '''1 2 28
    1 6 10
    2 3 16
    2 7 14
    3 4 12
    4 5 22
    5 6 25
    5 7 24
    7 4 18'''
    for i in inp.split('\n'):
        [u, v, w] = [int(j) for j in i.split()]
        g[u].append((v, w))
        g[v].append((u, w))
    print('graph g:')
    graph.print_graph(g)
    print()
    mst = kruskals(g)
    graph.print_graph(mst)
