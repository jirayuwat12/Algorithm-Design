import graph

g = graph.get_connected_graph(100,0.95)

def Kasaraju():
    '''
    done DFS and keep the finished node in the stack
    then, reverse direction on graph and do DFS from the top of stack
    each group of SCC is the node that we can reach without popping the stack
    '''
    return

if __name__ == '__main__' :
    print('graph g:')
    graph.print_graph(g)