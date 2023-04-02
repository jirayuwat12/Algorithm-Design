import sys
import heapq
input = sys.stdin.readline

[n,a,b] = list(map(int, input().split()))
hole = dict()
for _ in range(n):
    [x,y] = list(map(int, input().split()))
    hole[(x,y)] = 1
dp = [[1e10 for _ in range(1001)] for _ in range(1001)]
def BFS():
    min_ans = 1e10
    q = [(0,a,b)]
    while len(q) and q[0][0] < min_ans:
        ans,x,y = heapq.heappop(q)
        if dp[x][y] > ans:
            dp[x][y] = ans
        else:
            continue
        if ans > min_ans or not (1<=x<=1000 and 1<=y<=1000):
            continue
        if x==1 or x == 1000 or y == 1 or y == 1000:
            min_ans = min(min_ans,ans+((x,y) in hole))
        else:
            heapq.heappush(q,(ans+((x,y) in hole),x+1,y))
            heapq.heappush(q,(ans+((x,y) in hole),x-1,y))
            heapq.heappush(q,(ans+((x,y) in hole),x,y+1))
            heapq.heappush(q,(ans+((x,y) in hole),x,y-1))
        
    return min_ans
print(BFS())
            