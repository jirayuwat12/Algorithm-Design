import sys
input = sys.stdin.readline

[n,m] = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
dp = [list(map(int, input().split())) for _ in range(n+1)]

i = n
j = m

ans = []
while dp[i][j]!=0:
    if j-w[i-1] >= 0 and dp[i-1][j-w[i-1]] + v[i-1] == dp[i][j]:
        ans += [i]
        j-=w[i-1]
    i-=1

print(len(ans))
for i in ans:
    print(i,end=' ')
