def fact(n):
    def fact_iter(n, acc):
        if n == 0:
            return acc
        else:
            return fact_iter(n-1, n*acc)
    return fact_iter(n, 1)

if __name__ == '__main__':
    print(fact(5))


#fact-rec
def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)

# fact-acc
def fact_acc(n):
    acc = 1
    for i in range(1, n+1):
        acc *= i
    return acc

if __name__ == '__main__':
    print(fact_rec(5))
    print(fact_acc(5))

def fact_acc(n, acc):
    if n == 0:
        return acc
    else:
        return fact_acc(n-1, n*acc)

def fact (n):
    return fact_acc(n, 1)

def fact_iter(n):
    acc = 1
    while n > 1:
        acc *= n
        n -= 1
    return acc


if __name__ == '__main__':
    print(fact_iter(5))
    print(fact_iter(10))