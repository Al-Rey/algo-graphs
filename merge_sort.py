def MERGE(A, p, q, r):
    n1 = q-p+1
    n2 = r-q

    # array indexes will be 0 - nx
    L = [0]*(n1+1)
    R = [0]*(n2+1)

    for i in range(0, n1):
        L[i] = A[p+i]

    for j in range(0, n2):
        R[j] = A[q+j+1]

    L[n1] = float("inf")
    R[n2] = float("inf")

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def MERGE_SORT(A, p, r):
    if p < r:
        q = (p+r)//2
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q+1, r)
        MERGE(A, p, q, r)


if __name__ == "__main__":
    X = [4, 890, 34, 6, -9, 0, 2, 23]
    MERGE_SORT(X, 0, len(X)-1)
    print(X)