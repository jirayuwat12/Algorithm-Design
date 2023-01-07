# sorting

## problem

input:
- Array `A[1..n]` of `n` numbers
output:
- Array `A[1..n]` sorted in non-decreasing order (A[i] <= A[i+1]) for i = 1..n-1

example:
- input: `A = [3, 2, 1, 4, 5]`
- output: `A = [1, 2, 3, 4, 5]`

## algorithm

-------------------
|algorithm|time|space|
|---------|----|-----|
|[bubble sort]()|O(n^2)|O(1)|
|[selection sort](selection_sort.cpp)|O(n^2)|O(1)|
|[heap sort](heap_sort.cpp)|O(nlogn)|O(1)|
|[insertion sort](insertion_sort.cpp)|O(n^2)|O(1)|
|[radiix sort]()|O(n)|O(n)|
|[merge sort]()|O(nlogn)|O(n)|
|[quick sort]()|O(nlogn)|O(logn)|
|etc.|etc.|etc.|

<u>note</u>: merge sort and quick sort are devide and conquer algorithms ( D&C )

 