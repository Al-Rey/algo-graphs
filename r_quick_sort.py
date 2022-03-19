import random as rand
from quick_sort import PARTITION


def RANDOMIZED_PARTITION(A, p, r):
    rand.seed(40)
    i = rand.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return PARTITION(A, p, r)


def RANDOMIZED_QUICKSORT(A, p, r):
    if p < r:
        q = RANDOMIZED_PARTITION(A, p, r)
        RANDOMIZED_QUICKSORT(A, p, q-1)
        RANDOMIZED_QUICKSORT(A, q+1, r)


if __name__ == "__main__":
    X = [4, 890, 34, 6, -9, 0, 2, 23]
    RANDOMIZED_QUICKSORT(X, 0, len(X)-1)
    print(X)