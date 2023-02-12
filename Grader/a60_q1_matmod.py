
[n,k] = [int(i) for i in input().split()]

[a,b,c,d] = [int(i) for i in input().split()]

m = [[a,b],[c,d]]

def mul_m(a,b):
    ret = [[0,0],[0,0]]
    ret[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0])%k
    ret[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1])%k
    ret[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0])%k
    ret[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1])%k
    return ret

def pow_m(m,n):
    if n == 2:
        return mul_m(m,m)
    elif n == 1:
        return m
    else:
        if n%2 == 0:
            return pow_m(mul_m(m,m), n//2)
        else:
            return mul_m(m, pow_m(mul_m(m,m), n//2))
ret = pow_m(m,n)

print(ret[0][0], ret[0][1], ret[1][0], ret[1][1])
