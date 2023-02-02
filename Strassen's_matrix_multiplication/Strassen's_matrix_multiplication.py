import numpy

def Strassen(A,B):
    n = len(A)
    if n == 1:
        return A*B
    else:
        # Split A and B into 4 sub-matrices
        A11 = A[:n//2,:n//2]
        A12 = A[:n//2,n//2:]
        A21 = A[n//2:,:n//2]
        A22 = A[n//2:,n//2:]
        B11 = B[:n//2,:n//2]
        B12 = B[:n//2,n//2:]
        B21 = B[n//2:,:n//2]
        B22 = B[n//2:,n//2:]

        M1 = Strassen(A11+A22,B11+B22)
        M2 = Strassen(A21+A22,B11)
        M3 = Strassen(A11,B12-B22)
        M4 = Strassen(A22,B21-B11)
        M5 = Strassen(A11+A12,B22)
        M6 = Strassen(A21-A11,B11+B12)
        M7 = Strassen(A12-A22,B21+B22)

        C11 = M1+M4-M5+M7
        C12 = M3+M5
        C21 = M2+M4
        C22 = M1-M2+M3+M6

        C = numpy.zeros((n,n))
        C[:n//2,:n//2] = C11
        C[:n//2,n//2:] = C12
        C[n//2:,:n//2] = C21
        C[n//2:,n//2:] = C22

        return C


if __name__ == "__main__":
    # Read input
    n = int(input())
    A = numpy.array([list(map(int, input().split())) for _ in range(n)], dtype=numpy.int64)
    B = numpy.array([list(map(int, input().split())) for _ in range(n)], dtype=numpy.int64)


    print("numpy result:")
    for row in numpy.dot(A,B):
        print(*row,sep='\t')

    print("Strassen's result:")
    for row in Strassen(A,B):
        print(*row,sep='\t')

    print("numpy result == Strassen's result:", numpy.allclose(numpy.dot(A,B), Strassen(A,B)))

'''
Input:
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:
90 100 110 120
202 228 254 280
314 356 398 440
426 484 542 600

'''