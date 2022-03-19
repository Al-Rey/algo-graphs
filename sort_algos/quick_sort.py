"""

"""
def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def QUICKSORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)

        QUICKSORT(A, p, q-1)
        QUICKSORT(A, q+1, r)

if __name__ == "__main__":
    X = [4, 890, 34, 6, -9, 0, 2, 23]
    QUICKSORT(X, 0, len(X)-1)
    print(X)