import sys
input = sys.stdin.readline

[n, k] = list(map(int, input().split()))
s = list(map(int, input().split()))

dp = [0]*(n+1)

dp[0] = 1

for i in range(1,n+1):
    ret = 0
    for j in s:
        if i - j < 0 :
            continue
        ret += dp[i-j]
    dp[i] = ret

print(dp[-1] % 1000003)