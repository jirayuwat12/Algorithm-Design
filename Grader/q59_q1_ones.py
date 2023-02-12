n = int(input())

flag = 1

while n >= flag:
    flag = flag*10 + 1
flag = -(flag//10)

ans = 0
while n != 0 :
    n += flag
    ans += len(str(flag))-(str(flag)[0] == '-')
    
    while n != 0 and abs(n) < abs(flag):
        flag = flag//10
    if n < 0:
        flag = abs(flag)
    else:
        flag = -abs(flag)
print(ans)