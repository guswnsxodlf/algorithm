# Created by Jello on 2017. 6. 7.
def solution(A):
    cnt = 0
    for i in xrange(len(A)-1):
        if A[i] == A[i+1]:
            cnt += 1

    print('cnt: {}'.format(cnt))

    r = cnt

    # one of the coins must be reversed -> initial maximum 0
    max_r = 0

    for i in xrange(len(A)):
        if i > 0:
            if A[i-1] != A[i]:
                r += 1
            else:
                r -= 1
        if i < len(A)-1:
            if A[i+1] != A[i]:
                r += 1
            else:
                r -= 1

        max_r = max(max_r, r)
        print('r: {}, max_r: {}, i: {}'.format(r, max_r, i))
        r = cnt

    return max_r

print(solution([0,0,1,1,1,1]))
