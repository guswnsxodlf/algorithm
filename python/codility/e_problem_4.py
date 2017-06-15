# Created by Jello on 2017. 6. 14.

import math

def solution(N):
    a = N
    th = 10
    r = 0
    while True:
        if a >= th - 1:
            r += (th // 10) + (int(th * 0.09) * (int(math.log10(th)) - 1))
            th *= 10
        else:
            break

    for i in xrange(th // 10, a + 1):
        r += str(i).count('1')

    return r