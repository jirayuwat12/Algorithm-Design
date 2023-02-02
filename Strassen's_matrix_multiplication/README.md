# Strassen's Matrix Multiplication
<u>note</u>: Invented by Volker Strassen in 1969.

## The Problem
- Given two n x n matrices A and B, compute the product AB.

## Input
- The first line contains a single integer n (1 ≤ n ≤ 2000), the size of the matrices.
- The next n lines contain n integers each, the elements of matrix A.
- The next n lines contain n integers each, the elements of matrix B.

## Output
- Output n lines, each containing n integers, the elements of the product matrix AB.

## Sample Input
```
3
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9

```

## Sample Output
```
30 36 42
66 81 96
102 126 150
```

## Solution
### [Block Matrix Multiplication](https://en.wikipedia.org/wiki/Block_matrix)
- divide the matrices into 4 blocks 
$$ A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} $$
$$ B = \begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} $$
$$ C = \begin{bmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{bmatrix} $$

- then we have
$$ C_{11} = A_{11}B_{11} + A_{12}B_{21} $$
$$ C_{12} = A_{11}B_{12} + A_{12}B_{22} $$
$$ C_{21} = A_{21}B_{11} + A_{22}B_{21} $$
$$ C_{22} = A_{21}B_{12} + A_{22}B_{22} $$

<u>note</u> : we can each one recursively. -> **Divide and Conquer**
but O(n^3) is too slow.

### [Strassen's Matrix Multiplication](https://en.wikipedia.org/wiki/Strassen_algorithm)

$$ A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} $$
$$ B = \begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} $$
$$ C = \begin{bmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{bmatrix} $$

- divide the matrices into 7 blocks
1. M1 = (A1,1 + A2,2) (B1,1 + B2,2)
2. M2 = (A2,1 + A2,2) B1,1
3. M3 = A1,1 (B1,2 - B2,2)
4. M4 = A2,2 (B2,1 - B1,1)
5. M5 = (A1,1 + A1,2) B2,2
6. M6 = (A2,1 - A1,1) (B1,1 + B1,2)
7. M7 = (A1,2 - A2,2) (B2,1 + B2,2)

- then we have
$$ C_{11} = M1 + M4 - M5 + M7 $$
$$ C_{12} = M3 + M5 $$
$$ C_{21} = M2 + M4 $$
$$ C_{22} = M1 - M2 + M3 + M6 $$
- then Big-O = O(n^2.8074) -> O(n^2.8) -> O(n^2.8logn) -> O(n^2logn)
- [code](Strassen's_matrix_multiplication.py)

### Optional : [Strassen's Matrix Multiplication with Coppersmith-Winograd](https://en.wikipedia.org/wiki/Coppersmith%E2%80%93Winograd_algorithm)
