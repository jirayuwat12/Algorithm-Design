n = int(input())
a = 0
b = 1

n-=1
while n:
    a,b = b,a+b
    n-=1

print(b)