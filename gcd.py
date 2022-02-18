def gcd_rec(a, b):
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)

def gcd_acc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    print(gcd_rec(12, 18))
    print(gcd_acc(12, 18))
    print(gcd_iter(18, 12))