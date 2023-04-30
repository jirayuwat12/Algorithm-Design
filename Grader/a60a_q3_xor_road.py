import sys
input = sys.stdin.readline

n = int(input())
code = []
for i in range(n):
    code.append(int(input()))

edges = []
for i in range(n):
    for j in range(i+1,n):
        edges.append((code[i]^code[j],i,j))
edges = sorted(edges,key=lambda x : (-1*x[0],x[1],x[2]))

pr = [i for i in range(n)]
rank = [0 for i in range(n)]

mst_w = 0
idx = 0 
e = 0 
while e < n-1:
    u = edges[idx][1]
    v = edges[idx][2]
    w = edges[idx][0]
    idx += 1
    
    anc_u = u
    while pr[anc_u] != anc_u: anc_u = pr[anc_u]
    anc_v = v
    while pr[anc_v] != anc_v: anc_v = pr[anc_v]
    
    if anc_u != anc_v : 
        mst_w += w
        # union
        if rank[anc_u] > rank[anc_v]:
            pr[anc_v] = anc_u
        elif rank[anc_v] > rank[anc_u]:
            pr[anc_u] = anc_v
        else:
            pr[anc_u] = anc_v
            rank[anc_v] += 1
        e += 1

print(mst_w)
