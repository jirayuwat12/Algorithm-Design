import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())

dp = dict()
def recurr(l,state):
    print(l,state)
    if l == n:
        return 1
    else:
        l += 1
        ret = 0
        if state == 0:
            ret = (recurr(l,0) if (l,0) not in dp else dp[(l,0)]) + \
                (recurr(l,1) if (l,1) not in dp else dp[(l,1)])
        elif state == 1:
            ret = (recurr(l,2) if (l,2) not in dp else dp[(l,2)]) + \
                (recurr(l,1) if (l,1) not in dp else dp[(l,1)])
        else:
            ret = (recurr(l,0) if (l,0) not in dp else dp[(l,0)])
        dp[(l-1,state)] = ret  % 100000007
        return ret % 100000007
print((recurr(1,0) + recurr(1,1))%100000007)

'''
1 0 1
1 2 3
'''