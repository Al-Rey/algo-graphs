"""

"""
global A_heap_size

def LEFT(i):
    return 2*i


def RIGHT(i):
    return 2*i + 1


def MAX_HEAPIFY(A, i):
    largest = 0
    l = LEFT(i)
    r = RIGHT(i)

    if l < A_heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < A_heap_size and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A, largest)


def BUILD_MAX_HEAP(A):
    global A_heap_size
    A_heap_size = len(A)
    for i in range((len(A)-1)//2, -1, -1):
        MAX_HEAPIFY(A, i)


def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    for i in range(len(A)-1, -1, -1):
        A[0], A[i] = A[i], A[0]
        global A_heap_size
        A_heap_size -= 1
        MAX_HEAPIFY(A, 0)



if __name__ == "__main__":
    X = [4, 890, 34, 6, -9, 0, 2, 23]
    HEAPSORT(X)
    print(X)