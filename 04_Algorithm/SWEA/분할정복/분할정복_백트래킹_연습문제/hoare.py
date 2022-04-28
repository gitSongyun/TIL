def hoare(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:

        while i <= j and A[i] <= p:
            i += 1

        while i <= j and A[j] >= p:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j

def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s + 1, r)


A = [11, 45, 23, 81, 28, 34]
qsort(A, 0, len(A)-1)
print(A)
