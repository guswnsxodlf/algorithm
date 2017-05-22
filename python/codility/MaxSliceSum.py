# Created by Jello on 2017. 5. 22.

def solution(A):
    sum = r = A[0]
    for i in xrange(1,len(A)):
        sum = max(A[i], sum+A[i])
        r = max(r, sum)
    return r
