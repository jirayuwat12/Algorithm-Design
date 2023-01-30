n = int(input())
l = [int(i) for i in input().split()]
max_sum = -1
now_sum = 0
for i in l:
    if now_sum + i > 0:
        now_sum += i
        max_sum = max(max_sum,now_sum)
    else :
        now_sum = 0

print(max_sum)