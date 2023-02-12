import sys

n = int(input())

a= []

for i in range(n):
    [x,y] = [int(x) for x in sys.stdin.readline().split()]
    a.append([x,y])

a.sort(key=lambda x: x[0], reverse=True)

pareto = a[0]
ans = 1
for i in range(1, len(a)):
    if a[i][1] >= pareto[1]:
        pareto = a[i]
        ans += 1
print(ans)