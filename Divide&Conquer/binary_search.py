import random

# a is a sorted random list
# x is the number to be searched
# return the index of x in a
# return -1 if x is not in a

def binary_search(a, x):
    if len(a) == 0:
        return -1
    mid = len(a) // 2  
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a[:mid], x)
    else:
        index = binary_search(a[mid+1:], x)
        if index == -1:
            return -1
        else:
            return mid + 1 + index


if __name__ == "__main__":
    a = [random.randint(1,1000) for i in range(100)]
    if 100 not in a :
        a.append(100)
    a.sort()
    print(a)
    print(binary_search(a, 100))
