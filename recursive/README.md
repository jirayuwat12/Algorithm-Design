# Recursive


example

```cpp
void print_tri(int n) {
    if (n == 0) return;
    print_tri(n - 1);
    for (int i = 0; i < n; i++) {
        cout << "*";
    }
    cout << endl;
}
```
output : for `print_tri(4)`
```
****
***
**
*
```
hence, $T(n)$ is 
$$
T(n) = \begin{cases}
n+T(n+1) & \text{; } n \leq max\\
0 & \text{;n > max}
\end{cases}
$$

## There are 3 ways to compute solution of T(n)

1. Using (non-)homogeneous linear recurrence relations 
1. Using summation and subtitution method
    - <u>note</u>: use recursion tree
1. Using master theorem (or master method)

## 3. Using master theorem (or master method)

in case
$$
T(n) = aT(\frac{n}{b}) + \Theta(n^d)
$$
where $a \geq 1, b > 1, d \geq 0$ and $T(0) = 1 $

**then**
$$
T(n) = \begin{cases}
\Theta(n^c) & \text{; } n^d < n^c\\
\Theta(n^clogn) & \text{; } n^d = n^c\\
\Theta(n^{d}) & \text{; } n^d > n^c
\end{cases}
$$
where $c = \log_b a$

>the meaning of $T(n)$ is "There are $a$ problems with size $\frac{n}{b}$ and this problem takes $\Theta(n^d)$ time to solve" 