a = input()
b = input()

def check(a,b):
    if a == b:
        return True
    elif len(a) == 1 or len(b) == 1 or len(a) != len(b):
        return False
    else:
        a1 = a[:len(a)//2]
        a2 = a[len(a)//2:]
        b1 = b[:len(b)//2]
        b2 = b[len(b)//2:]
        if check(a1,b1) and check(a2,b2):
            return True
        elif check(a1,b2) and check(a2,b1):
            return True
        else:
            return False

if check(a,b):
    print("YES")
else:
    print("NO")
