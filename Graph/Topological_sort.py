import graph

g = graph.get_connected_graph(10,0.7)

def topological_sort(graph):
    __sorted = list()
    __visited = dict()
    for n in graph:
        if n in __visited:
            continue
        stack = list()
        stack.append(n)
        while len(stack) != 0:
            __visited[stack[-1]] = True
            temp = stack[-1]
            no_push = True
            for ch in graph[temp]:
                if ch not in __visited:
                    stack.append(ch)
                    no_push = False
            if no_push:
                __sorted.append(temp)
                stack = stack[:-1]
    return __sorted[::-1]
            
if __name__ == '__main__':
    g = dict()
    g['A'] = ['C']
    g['B'] = ['C','D']
    g['C'] = ['E']
    g['D'] = ['F']
    g['E'] = ['H','F']
    g['F'] = ['G']
    g['G'] = []
    g['H'] = []
    print(topological_sort(g))