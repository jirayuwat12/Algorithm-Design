import sys
input = sys.stdin.readline

[n,m] = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        from_left = (a[i][j] + dp[i][j-1]) if j-1 >= 0 else 0
        from_top = (a[i][j] + dp[i-1][j]) if i-1 >= 0 else 0
        from_diag = (a[i][j]*2 + dp[i-1][j-1]) if i-1>=0 and j-1>=0 else 0
        dp[i][j] = max([from_left,from_top,from_diag])
        if dp[i][j] == 0 :
            dp[i][j] = a[i][j]

print(dp[-1][-1])
