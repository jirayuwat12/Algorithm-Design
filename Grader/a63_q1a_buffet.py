import sys
input = sys.stdin.readline
[n,k,m] = list(map(int, input().split()))
d = list(map(int, input().split()))
qs = [0,d[0]]
for i in d[1:]:
    qs += [qs[-1] + i]
question = []
for _ in range(k):
    t = list(map(int, input().split()))
    question += [t]

for t in question:
    [p,w] = t
    # print(f'p = {p}, w = {w}')
    l = p-1
    p -=1
    r = n-1
    while r-l > 1:
        mid = (r+l) //2
        deli = qs[mid+1] - qs[p] - m*(mid-p+1)
        # print(f'l = {l}, r = {r}, mid = {mid}, deli = {deli}')
        if deli < w:
            l = mid + 1
        else:
            r = mid
    ans = 0
    if qs[l+1] - qs[p] - m*(l-p+1) >= w:
        ans = l
    else :
        ans = r
    print(ans+1)