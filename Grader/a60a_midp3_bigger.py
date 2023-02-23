import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
hash = dict()
hash[0] = c[0]
hash[1] = max(c[0],c[1])
hash[2] = max(hash[1],c[2])
for i in range(3,n):
    inc = c[i] + hash[i-3]
    exc = max(hash[i-1],hash[i-2])
    hash[i] = max(inc,exc)
print(hash[n-1])