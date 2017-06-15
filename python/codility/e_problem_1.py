# Created by Jello on 2017. 6. 14.

def solution(A):
    one = 0
    zero = 0
    for v in A:
        if v == 1:
            one += 1
        else:
            zero += 1

    return min(one, zero)