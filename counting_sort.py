
def COUNTING_SORT(A, B, k):
    C = [0 for i in range(0, k+1)]

    for j in range(0, len(A)):
        C[A[j]] += 1

    # C[i] now contatins the number of elements equal to i
    for i in range(0, k+1):
        C[i] = C[i] + C[i-1]

    # C[i] now contains the number of elements less than or equal to i
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-2] = A[j]
        C[A[j]] -= 1


if __name__ == "__main__":
    X = [4, 0, 8, 6, 9, 0, 2, 23]
    B = [0]*len(X)
    COUNTING_SORT(X, B, 23)
    print(B)
