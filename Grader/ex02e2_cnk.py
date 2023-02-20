[n,k] =[int(i) for i in input().split()]

dp = [[ 0 for i in range(k+1)] for i in range(n+1)]

def b(n,k):
    if dp[n][k] != 0:
        return dp[n][k]
    else:
        ret = 0
        if n==k or k == 0:
            ret = 1
        else:
            ret = b(n-1,k-1) + b(n-1,k)
        dp[n][k] = ret
        return dp[n][k]
print(b(n,k))