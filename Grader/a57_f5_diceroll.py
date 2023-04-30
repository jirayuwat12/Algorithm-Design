import sys
from collections import deque
input = sys.stdin.readline


def roll_dice(dice, direction):
    '''
          [1]
    [2] [dice] [3]
          [4]
    '''
    dice = list(dice)
    if direction == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    if direction == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    if direction == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    if direction == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]

    return dice, dice[0]


[R, C, p, q] = list(map(int, input().split()))
dice = list(map(int, input().split()))

dp = dict()
ret = 1e10

queue = deque()
queue.append((dice, 0, 0, 0))
while len(queue):
    dice, i, j, dist = queue.popleft()
    if i == p and j == q:
        ret = min(ret, dist)
    # check for negative loop
    if (i, j) in dp :
        if dp[(i,j)][0] > dist:
            dp[(i,j)] = [dist,dp[(i,j)][1] + 1]
        if dp[(i, j)][1] > R+C:
            ret = -1
            break
    # first found
    if (i, j) not in dp:
        dp[(i, j)] = [dist,0]
    # cannot
    if dist >= ret:
        continue
    
    for a, b in enumerate([[-1, 0], [0, -1], [0, 1], [1, 0]]):
        a += 1
        if 0 <= i+b[0] < R and 0 <= j+b[1] < C:
            k, l = roll_dice(dice, a)
            queue.append((k, i+b[0], j+b[1], dist+l))

print(ret)
