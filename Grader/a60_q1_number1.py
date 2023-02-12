import sys

[n,l,r] = [int(x) for x in sys.stdin.readline().split()]

'''
if n > 1 then replace n with [floor(n/2), n mod 2, floor(n/2)]
repeat until all numbers are 1,0
then count the number of 1s in the list that in range [l,r] 1-indexed
using divide and conquer
'''
# solution
def count_ones(n,l,r):
    if n == 1:
        return 1
    else:
        mid = 2**(n-1)
        if r <= mid:
            return count_ones(n-1,l,r)
        elif l > mid:
            return count_ones(n-1,l-mid,r-mid)
        else:
            return count_ones(n-1,l,mid) + count_ones(n-1,1,r-mid)

print(count_ones(n,l,r))
