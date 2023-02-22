import sys
input = sys.stdin.readline

[n,m] = list(map(int, input().split()))

a = []
for i in range(n):
    a.append(int(input()))

print(a)

'''
    0   1   r(2)    r(3)    2   r(5)    r(6)    
3   9   4   ....    ....    1   ....    ....
3   9   13  ....    ....    8   
1   1
'''