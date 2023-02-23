import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

dp = [1]
for i in range(1,n):
    cmp_list = [dp[j] for j in range(i) if s[i] > s[j]]
    if len(cmp_list) == 0:
        dp.append(1)
    else:
        dp.append(max(cmp_list)+1) 
  
print(max(dp))
'''
    3   1   4   5   2
    1   0   2   3   1
'''