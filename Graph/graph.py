import random

# generate graph
# in adjacency list format

def get_connected_graph(n_vertice,noise = 0,weighted = False):
    '''
    generate a connected graph with n_vertice vertices
    if noise == 0, the graph is a complete graph
    if noise == 1, the graph is a complete graph with no edges
    if 0 < noise < 1, the graph is a complete graph with some edges removed

    n_vertice: int
    noise: float
    weighted: bool
    return: dict

    '''
    graph = {}
    for i in range(n_vertice):
        graph[i] = []
        for j in range(n_vertice):
            if i != j:
                if random.random() < noise:
                    continue
                if weighted:
                    graph[i].append((j,random.random()))
                else:
                    graph[i].append(j)
    return graph

def get_tree(n_vertice,weighted = False):
    '''
    generate a tree with n_vertice vertices
    if weighted == True, the tree is weighted

    n_vertice: int
    weighted: bool
    return: dict

    '''
    graph = {}
    for i in range(n_vertice):
        graph[i] = []
        if i != 0:
            connectNode = random.randint(0,i-1)
            if weighted:
                graph[i].append((connectNode,random.random()))
            else:
                graph[i].append(connectNode)
    return graph

def print_graph(graph):
    for i in graph:
        print(i,graph[i])