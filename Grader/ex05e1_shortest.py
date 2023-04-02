import sys
input = sys.stdin.readline

[r,c] = list(map(int, input().split()))
m = list()
for _ in range(r):
    m.append(input())

def BFS(row = 0,col = 0):
    q = [(0,row,col)]
    visited = dict()
    while len(q) != 0:
        d,i,j = q.pop(0)
        if (i,j) in visited:
            continue
        visited[(i,j)] = True
        if i == r-1 and j == c-1 :
            return d
        # if i-1 >= 0 and m[i-1][j] == '.' and (i-1,j) not in visited:
        #     q.append((d+1,i-1,j))

        if i+1 < r and m[i+1][j] == '.' and (i+1,j) not in visited:
            q.append((d+1,i+1,j))

        if j-1 >= 0 and m[i][j-1] == '.' and (i,j-1) not in visited:
            q.append((d+1,i,j-1))

        if j+1 < c and m[i][j+1] == '.' and (i,j+1) not in visited:
            q.append((d+1,i,j+1))
    return -1

print(BFS())