import sys
[n,w] = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.readline().split()]
#  find MCS of a with max w elements
#  divide and conquer

prev_sum = [a[0]]
for i in range(1,n):
    prev_sum.append(prev_sum[-1]+a[i])

mcs = -1001

def mcs_with_w(prev_sum,w):
    global mcs
    for i in range(n-w):
        mcs = max(mcs,prev_sum[i+w-1]-(prev_sum[i-1] if i-1 >= 0 else 0))
for i in range(1,w+1):
    mcs_with_w(prev_sum,i)
print(mcs)