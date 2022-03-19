"""

"""
def INSERTION_SORT(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[1....j-1]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1

        A[i+1]=key

if __name__ == "__main__":
    X = [4, 890, 34, 6, -9, 0, 2, 23]
    INSERTION_SORT(X)
    print(X)