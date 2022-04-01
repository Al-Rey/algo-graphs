"""
Author: Al-Rey
Desc: This program implements the selection sort
"""

def SELECTION_SORT(data):
    if len(data) == 1:
        return data[0]

    minimum = data[0]
    min_index = 0
    
    for ii  in range(0, len(data)):
        minimum = data[ii]
        min_index = ii
        for jj in range(ii, len(data)):
            if data[jj] <= minimum:
                minimum = data[jj]
                min_index = jj
    
        if minimum != data[ii]:
            temp = data[ii]
            data[ii] = minimum

            data[min_index] = temp
            

if __name__ == "__main__":
    X = [4, 890, 34, 6, 9, 0, 2, 23]
    SELECTION_SORT(X)
    print(X)
