import graph

g = graph.get_connected_graph(5,0,weighted=True)

'''
DFS & BFS -> adj list -> topo sort
MST -> any -> edge list
Shortest Path -> matrix

'''

def bellman(g):
    dist = [1e20] * len(g)
    # edge list
    edge_list = []
    for u in g:
        for v in u:
            v,w = v
            edge_list.append(w,u,v)

    for _ in range(len(g)): #O(n)
        for edge in edge_list: # O(e)
            w,u,v = edge
            if dist[v] > dist[u] + find(u,v):
                dist[v] = dist[u] + find(u,v)
    # O(ne) ->O(n^2)
    return dist


graph.print_graph(g)

print(bellman(g))
