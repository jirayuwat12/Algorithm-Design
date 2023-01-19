# Divide & Conquer

## Key idea
- solve problem instance by **divide** it into smaller instances and **conquer** them recursively
- use **merge** to combine the solutions of the subproblems

## Table of Contents
- [Example](#example)
- [method](#method)
- [binary search](#binary-search)
    - [version 1 : minus 1](#version-1--minus-1)
    - [version 2 : divide 2](#version-2--divide-2)

## Example
- merge sort
- quick sort
- [binary search](binary_search.py)

```python
# problem : sort list
def merg_sort(v):
    if len(v) <= 1:
        return v
    mid = len(v) // 2
    # divide
    left = merg_sort(v[:mid])
    right = merg_sort(v[mid:])
    # conquer
    return merge(left, right)

def merge(left, right):
    result = []
    # problem is merge two sorted list
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

```

## Method
1. divide problem into subproblems
1. solve subproblems recursively
1. combine solutions of subproblems

## Binary search
- search for a key in a sorted list
### version 1 : minus 1

a = sorted list

x = key

return index of x in a if x is in a, otherwise return -1

```python
def bs(a,x):
    if a == []:
        return -1
    elif a[0] == x:
        return 1
    else :
        temp = bs(a[1:],x)
        if temp == -1:
            return -1
        else:
            return temp + 1
# O(n)
```

### version 2 : divide 2
a = sorted list

x = key

return index of x in a if x is in a, otherwise return -1

[code](binary_search.py)

```python
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
#O(logn)
```

## Merge sort

> code is [here](../sorting/merge_sort.py)

$ T(n) = 2T(\frac{n}{2}) + \Theta(n) $

$hence, T(n) = \Theta(nlogn) $