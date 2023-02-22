import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def ms(a : list):
    ret = a[0]
    s = 0
    for i in range(len(a)):
        s += a[i]
        ret = max(ret,s)
        if s < 0 :
            s = 0
    return ret

ans = -1e3

for i in range(n-1):
    list1 = [a[j][i+j] for j in range(n-i)]
    list2 = [a[i+j][j] for j in range(n-i)]
    ans = max([ans,ms(list1),ms(list2)])

print(ans)    