import sys
input = sys.stdin.readline

[n,m] = [int(i) for i in input().strip().split()]
a = [int(i) for i in input().strip().split()]

dp = [[0] + [m]*(m)]

for v in (a):
    dp.append([0])
    for j in range(1,m+1):
        if j-v >= 0:
            app = min(dp[-1][j-v]+1,dp[-2][j])
        else:
            app = dp[-2][j]
        dp[-1].append(app)

print(dp[-1][-1])
'''
13 - 5 4 1
    0   1   2   3   4   5   6   7   8   9   10  11  12  13
0   0   999 999 999 999 999 999 999 999 999 999 999 999 999
5   0   999 999 999 999 1   999 999 999 999 2   999 999 999   
4   0   999 999 999 1   1   999 999 2   2   2   999 2   999
1   0   1   2   3   1   1   2   3   2   2   2   3   2   3
'''