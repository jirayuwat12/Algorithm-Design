n = int(input())

l = [2]

for i in range(10):
    l = l + [l[len(l)//2]+1] + l

print(sum(l)+len(l))
