# Created by Jello on 2017. 5. 18.

def solution(A):
    A.sort()
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0
