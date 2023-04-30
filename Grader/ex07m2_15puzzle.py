import sys
from collections import deque
import heapq
input = sys.stdin.readline


def complete(board):
    idx = 1
    for i in board:
        for j in i:
            if j == idx:
                idx += 1
            elif idx != 16:
                return False
    return True

# number of move that we need to solve at least
def score(board):
    ret = 0
    idx = 1
    for i in board:
        for j in i:
            if j != idx:
                ret += 1
            idx += 1
    return ret


board = [list(map(int, input().split())) for _ in range(4)]

i = 0
j = 0
for x in range(4):
    for y in range(4):
        if board[x][y] == 0:
            i = x
            j = y

visited = set()

q = []
q.append((score(board), score(board), 0, board, i, j, (-1, -1)))
ans = 1e10

while len(q):
    top = heapq.heappop(q)
    _, sc, moves, board, i, j, last_move,  = top
    print(top,ans)
    # check visited
    if str(board) in visited:
        continue
    else:
        visited.add(str(board))
    # check for complete
    if i == 3 and j == 3 and complete(board):
        ans = min(moves, ans)
        continue
    # moves
    for m in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        if -1*m[0] == last_move[0] and -1*m[1] == last_move[1]:
            continue
        if 0 <= i+m[0] < 4 and 0 <= j+m[1] < 4:
            b = list()
            for k in board:
                b.append(list(k))
            b[i][j], b[i+m[0]][j+m[1]] = b[i+m[0]][j+m[1]], b[i][j]
            if score(b) + moves + 1 < ans:
                heapq.heappush(q, (score(b) + moves + 1,score(b), moves + 1, b, i+m[0], j+m[1], m))

print(ans)
