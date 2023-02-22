import sys
input = sys.stdin.readline

n = int(input())
c = [int(i) for i in input().split()]

def solve(n,c):
    dp = []
    for i,v in enumerate(c):
        x = v
        if i - 3 >=0:
            x = dp[i-3] + v
        if i - 2 >= 0 :
            x = max(dp[i-2] + v,x)
        if i - 1 >= 0 :
            x = max(x,dp[i-1])
        dp.append(x)
    return dp[-1]
print(solve(n,c))
'''
48  1   3   95  2   1   3   44  22  2
48  48  51  143 143 144 146 188 
'''