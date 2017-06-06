# Created by Jello on 2017. 6. 7.
import math

def solution(A, B):
    if B < 0:
        return 0

    if A < 0:
        a = 0
    else:
        a = int(math.ceil(math.sqrt(A)))

    b = int(math.floor(math.sqrt(B)))
    return b-a+1

print(solution(int(input()), int(input())))
