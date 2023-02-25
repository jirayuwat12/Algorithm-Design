import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))

dp = [0] * n
dp[0] = a[0]

for i in range(1, n):
    dp[i] = a[i] + max(dp[max(0,i-3):i])

print(dp[-1])