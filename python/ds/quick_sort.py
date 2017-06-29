# Created by Jello on 2017. 6. 29.
import time

def qsort(A):
    if len(A) <= 1:
        return A

    pivot = A[0]
    (less, equal, greater) = ([], [A[0]], [])

    for x in A[1:]:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return qsort(less) + equal + qsort(greater)

# test

print(qsort([1,4,2,6,10,38,12]))
print(qsort([9,18,23,53,77]))
print(qsort([88,1,4,0,43]))
print(qsort([100,3,78,6,223,1]))
