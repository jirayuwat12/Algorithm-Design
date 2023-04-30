import sys
input = sys.stdin.readline

def span(ghost,m,T,R,C):
    dist = T-ghost[0]
    q = [[0,ghost[1],ghost[2]]]
    while len(q) and q[0][0] <= dist:
        d,r,c = q.pop(0)
        m[r][c] = 'x'
        d+=1
        if r+1 < R and m[r+1][c] != '#':
            q.append([d,r+1,c])
        if r-1 >= 0 and m[r-1][c] != '#':
            q.append([d,r-1,c])
        if c+1 < C and m[r][c+1] != '#':
            q.append([d,r,c+1])
        if c-1 >= 0 and m[r][c-1] != '#':
            q.append([d,r,c-1])
        

K = int(input())
for _a in range(K):
    # input
    [R,C,n,T,r,c] = list(map(int, input().split()))
    ghosts = []
    m = []
    for _b in range(n):
        [ti,ri,ci] = list(map(int, input().split()))
        ghosts.append([ti,ri,ci])
    for _ in range(R):
        m.append(input())
    # span ghost 
    for ghost in ghosts:
        span(ghost,m,T,R,C)
    # show map
    for row in m:
        print(' '.join(map(str, row)))