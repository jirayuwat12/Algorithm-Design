[x,n,k] = [int(i) for i in input().split()]

def calc(x,n,k):
    if n < 10:
        return x**n % k
    else:
        if n-n//2 != n//2:
            return ( calc(x,n//2,k) * calc(x,n-n//2,k) ) % k
        else:
            return calc(x,n//2,k)**2 %k
print(calc(x,n,k))