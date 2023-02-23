import sys
input = sys.stdin.readline

[n,m] = list(map(int, input().split()))
X = input()
Y = input()
l = [list(map(int, input().split())) for _ in range(n+1)]

ret = ''
x, y = m,n

while l[y][x] != 0:
    if X[y-1] == Y[x-1]:
        ret += X[y-1]
        x-=1
        y-=1
    elif l[y-1][x] > l[y][x-1]:
        y-=1
    else:
        x-=1
print(ret[::-1])