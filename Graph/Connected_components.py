import graph
import BFSandDFS

g = graph.get_connected_graph(100, 0.95)


def get_all_component(graph):
    components = []
    visited = dict()
    for i in range(len(graph)):
        if i not in visited:
            components.append(BFSandDFS.BFS(graph, i))
            for j in components[-1]:
                visited[j] = True
    return components


if __name__ == '__main__':
    print('graph g :')
    graph.print_graph(g)

    print(get_all_component(g))
