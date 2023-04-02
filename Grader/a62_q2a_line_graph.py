import sys
input = sys.stdin.readline

[n,e] = list(map(int, input().split()))
# init adj list
adj_list = dict()
for i in range(n):
    adj_list[i] =[]
# read inp
for _ in range(e):
    [u,v] = list(map(int, input().split()))
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = dict()
ck = True
def spread(node,pr = -1):
    global visited
    visited[node] =True
    for ch in adj_list[node]:
        if ch not in visited:
            spread(ch,node)
        elif ch != pr:
            global ck
            ck = False
# spread to non-linear
for node in range(n):
    if node not in visited:
        if len(adj_list[node]) > 2:
            spread(node)
# print(visited)
# find ans
ret = 0
for node in range(n):
    if node not in visited:
        # print(f'spread {node}')
        ck = True
        spread(node)
        ret += ck
        # print(visited)
print(ret)