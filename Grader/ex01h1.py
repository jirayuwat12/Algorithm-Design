n = int(input())

while n:
    t = int(input())

    n-=1

a = [1,2,2,3,3,4,4,4,5,5,5]
for i in range(6,1000):
    for _ in range(a[i]):
        a.append(i)

for i in range(1000):
    print(i,a.count(i))