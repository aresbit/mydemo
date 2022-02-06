def selection_sort(A, i = None):
    if i is None: i = len(A) - 1
    if i == 0: return
    for j in range(i):
        if A[j] > A[i]:
            A[j], A[i] = A[i], A[j]
    selection_sort(A, i - 1)




# insertion_sort
def insertion_sort(A, i = None):
    if i is None: i = len(A) - 1
    if i == 0: return
    for j in range(i):
        if A[j] > A[i]:
            A[j], A[i] = A[i], A[j]
    insertion_sort(A, i - 1)


# merge_sort
def merge_sort(A, a=0, b = None):
    if b is None: b = len(A)
    if b - a <= 1: return
    m = (a + b) // 2
    merge_sort(A, a, m)
    merge_sort(A, m, b)
    merge(A, a, m, b)

def merge(A, a, m, b):
    L = A[a:m]
    R = A[m:b]
    i =len(L)
    j = len(R)
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b - 1] = L[i - 1]
            i -= 1
        else:
            A[b - 1] = R[j - 1]
            j -= 1
        merge(A, a, m, b - 1)


# quick_sort
def quick_sort(A, a=0, b=None):
    if b is None: b = len(A)
    if b - a <= 1: return
    m = partition(A, a, b)
    quick_sort(A, a, m)
    quick_sort(A, m, b)

def partition(A, a, b):
    x = A[b - 1]
    i = a
    for j in range(a, b - 1):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[b - 1] = A[b - 1], A[i]
    return i








if __name__ == "__main__":
    A = [1, 2, 3, -4, 10, -5, -9, 101, 32]
    quick_sort(A)
    print(A)
