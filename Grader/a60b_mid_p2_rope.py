import sys
input = sys.stdin.readline

[n,a,b,c] = list(map(int, input().split()))
l = [0]*(n+1)
for i in range(n+1):
    if not i % a:
        l[i] = i//a

for v in [b,c]:
    for i in range(v,n+1):
        l[i] = max([l[i],(1+l[i-v]) if l[i-v] != 0 else -1,i//v if i%v == 0 else -1])
    print(l)
print(l[-1])
'''
    0   1   2   3   4   5   6   7   8   9   10
2   0   0   1   0   2   0   3   0   4   0   5
3   0   0   1   1   2   2   3   3   4   4   5
4   0   0   1   1   2   2   3   3   4   4   5
'''