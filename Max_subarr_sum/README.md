# Maximum subarray sum

problem : [link](https://www.hackerrank.com/challenges/maxsubarray/problem)

## The problem
- Given an array of integers, find the maximum sum of the subarray.
- The subarray must be contiguous.

## input
- A[1..n] : array of integers

## output
- p, q : begin and end index of the subarray
- max_sum : maximum sum of the subarray

## example
- A = [-2, 1, -3, **4, -1, 2, 1**, -5, 4]
- p = 3, q = 6, max_sum = 6

## solution
| Algorithm | Time Complexity | code |
| --- | --- | --- |
| brute force | O(n^2) | [code](brute_force.py) |
| divide and conquer | O(nlogn) | [code](divide_and_conquer.py) |