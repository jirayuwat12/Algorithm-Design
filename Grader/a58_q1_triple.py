[n,m] = [int(i) for i in input().split()]

l = [int(i) for i in input().split()]

targets = [int(i) for i in input().split()]

def findTriplet(l, target):
    for i in range(len(l)-1):
        s = set()
        sum = target - l[i]
        for j in range(i+1, len(l)):
            if sum - l[j] in s:
                return True
            s.add(l[j])
    return False

for target in targets:
    if findTriplet(l, target):
        print("YES")
    else:
        print("NO")