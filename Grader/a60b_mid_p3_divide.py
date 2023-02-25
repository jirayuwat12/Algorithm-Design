import sys
import math
input = sys.stdin.readline

[n,k] = list(map(int, input().split()))

hash = dict()

def nCr(n,r):
    if r in [1,n]:
        return 1
    else:
        ret = (r*(hash[(n-1,r)] if (n-1,r) in hash else nCr(n-1,r)))%1997 + (hash[(n-1,r-1)] if (n-1,r-1) in hash else nCr(n-1,r-1))%1997
    # print(n,r,ret)
    hash[(n,r)] = ret
    return ret%1997

print(nCr(n,k))
