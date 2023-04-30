import sys
import heapq

input = sys.stdin.readline

[W, N] = list(map(float, input().split()))
v = list(map(float, input().split()))
w = list(map(float, input().split()))
data = [(w[i], v[i]) for i in range(int(N))]
data = sorted(data)

qs = [0 for i in range(int(N))]
qs[int(N)-1] = data[int(N)-1][1]
for i in range(int(N)-2,-1,-1):
    qs[i] = qs[i+1] + data[i][1]

ans = 0
sumw = 0
sumv = 0

def search(idx=0):
    global sumw,sumv,ans
    if idx == N or sumw + data[idx][0] > W:
        ans = max(ans, sumv)
        return
    if sumv + qs[idx] < ans:
        return 
    if sumw + data[idx][0] <= W:
        # deselect
        search(idx+1)
        # select
        sumw += data[idx][0]
        sumv += data[idx][1]
        search(idx+1)
        sumw -= data[idx][0]
        sumv -= data[idx][1]
 
search()

print(ans)
