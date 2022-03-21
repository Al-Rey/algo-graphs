from heapq import heapify
import time
import matplotlib.pyplot as plt
import random as rand
from pandas import array
from copy import deepcopy

from heap_sort import HEAPSORT
from insertion_sort import INSERTION_SORT
from merge_sort import MERGE_SORT
from quick_sort import QUICKSORT


array_sizes = [2**x for x in range(0,8)]
rand.seed(42)
insert_times = []
merge_times = []

for size in array_sizes:
    sort_base = [0]*size

    for ii in range(size):
        num = rand.randint(-255, 256)
        sort_base[ii] = num

    print("insertion Sort with %d elements" % size)
    sort = deepcopy(sort_base)
    start = time.time()
    INSERTION_SORT(sort)
    end = time.time()

    print("Time Elapsed: ", end-start)
    insert_times.append(end-start)
    print("")    

    print("Merge Sort with %d elements" % size)
    sort = deepcopy(sort_base)
    start = time.time()
    MERGE_SORT(sort, 0, len(sort)-1)
    end = time.time()
    # diff = end-start
    # print(sort1)
    print("Time Elapsed: ", end-start)
    merge_times.append(end-start)
    print("---------------------------")   



plt.plot(array_sizes, insert_times, label="insert")
plt.plot(array_sizes, merge_times, label="merge")
plt.legend()
plt.xlabel("Array Sizes")
plt.ylabel("Run Times")
plt.xticks([x for x in range(0, max(array_sizes)+10, 10)])
plt.grid()
plt.savefig("merge_vs_insert.png")