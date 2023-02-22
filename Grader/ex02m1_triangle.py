import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])

for i in range(1,n):
    for j in range(len(a[i])):
        if j-1 >= 0:
            a[i][j] += max(a[i-1][j] if j != len(a[i])-1 else -1, a[i-1][j-1])
        else:
            a[i][j] += a[i-1][j]


print(max(a[-1]))
