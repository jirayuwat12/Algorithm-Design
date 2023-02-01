# this code in python version cannot pass the Time Limit Exceeded test case
# but same code in c++ version can pass all test cases
[n,m] = [int(i) for i in input().split()]

l = [int(i) for i in input().split()]

targets = [int(i) for i in input().split()]

def findTriplet(l, target):
    for i in range(0,len(l)-1):
        second = i+1
        third = len(l)-1

        while(second < third):
            sum = l[i] + l[second] + l[third]
            if sum == target:
                return True
            elif sum < target:
                second += 1
            else:
                third -= 1
    return False

min_sum = l[0] + l[1] + l[2]
max_sum = l[-1] + l[-2] + l[-3]

for target in targets:
    if target < min_sum or target > max_sum:
        print("NO")
        continue
    if findTriplet(l, target):
        print("YES")
    else:
        print("NO")