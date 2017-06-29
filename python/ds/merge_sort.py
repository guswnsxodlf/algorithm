# Created by Jello on 2017. 6. 29.


def merge(left, right):
    result = []
    i = j = 0
    while len(left)-1 >= i or len(right)-1 >= j:
        if len(left)-1 >= i and len(right)-1 >= j:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif len(left)-1 < i:
            result.append(right[j])
            j += 1
        elif len(right)-1 < j:
            result.append(left[i])
            i += 1

    return result


def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

print(merge_sort([1,4,2,5]))
print(merge_sort([100,48,8,1,4,2,5,10,28]))
print(merge_sort([1,3,4,9,2,12,5,13]))
