import sys
import heapq
input = sys.stdin.readline

ans = set()
n = int(input())

board = [[0]*n for i in range(n)]


def place(i, j):
    global board
    # normal
    for k in range(n):
        board[i][k] += 1
        board[k][j] += 1
    # diag
    a, b = i, j
    while 0 <= a < n and 0 <= b < n:
        board[a][b] += 1
        a += 1
        b += 1
    a, b = i, j
    while 0 <= a < n and 0 <= b < n:
        board[a][b] += 1
        a -= 1
        b -= 1
    a, b = i, j
    while 0 <= a < n and 0 <= b < n:
        board[a][b] += 1
        a -= 1
        b += 1
    a, b = i, j
    while 0 <= a < n and 0 <= b < n:
        board[a][b] += 1
        a += 1
        b -= 1
    # self
    board[i][j] = -1


def deplace(i, j):
    global board
    # normal
    for k in range(n):
        board[i][k] -= 1
        board[k][j] -= 1
    # diag
    a, b = i, j
    while 0 <= a < n and 0 <= b < n:
        board[a][b] -= 1
        a += 1
        b += 1
    a, b = i, j
    while 0 <= a < n and 0 <= b < n:
        board[a][b] -= 1
        a -= 1
        b -= 1
    a, b = i, j
    while 0 <= a < n and 0 <= b < n:
        board[a][b] -= 1
        a -= 1
        b += 1
    a, b = i, j
    while 0 <= a < n and 0 <= b < n:
        board[a][b] -= 1
        a += 1
        b -= 1
    # self
    board[i][j] = 0


def search(q=0, x=0, y=0):
    global board, n, ans
    if q == n:
        ans.add(str(board))
        return
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                place(i, j)
                search(q + 1, i+1, j+1)
                deplace(i, j)


search()

print(len(list(ans)))
