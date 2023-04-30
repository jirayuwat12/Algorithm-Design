import sys
input = sys.stdin.readline

n = int(input())

ans = 0

visited = dict()

def search(last = 1,ls = 0):
    global ans
    if ls in visited:
        ans += visited[ls]
        return 
    if ls == n:
        ans += 1
        if ls not in visited:
            visited[ls] = 1
        else:
            visited[ls] += 1
        return

    for i in range(last,n+1):
        if ls + i > n:
            break
        else:
            search(i,ls+i) 

search()
print(ans)