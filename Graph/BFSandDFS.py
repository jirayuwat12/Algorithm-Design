import graph

g = graph.get_connected_graph(5, 0.8)


def BFS(graph, root):
    visited = dict()
    q = [root]
    ret = []
    while len(q) != 0:
        if q[0] in visited:
            q.pop(0)
            continue
        ret.append(q[0])
        visited[q[0]] = True
        for node in graph[q[0]]:
            q.append(node)
        q.pop(0)
    return ret


def DFS(graph, root):
    visited = dict()
    q = [root]
    ret = []
    while len(q) != 0:
        if q[-1] in visited:
            q.pop(-1)
            continue
        temp = q[-1]
        ret.append(temp)
        visited[temp] = True
        q.pop(-1)
        for node in graph[temp]:
            q.append(node)
    return ret


if __name__ == '__main__':
    print('graph g:')
    graph.print_graph(g)
    print(f'BFS at 0 = {BFS(g,0)}')
    print(f'DFS at 0 = {DFS(g,0)}')
