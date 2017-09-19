# Created by Jello on 2017. 9. 19.
import math
import sys

T = int(sys.stdin.readline())

while T > 0:
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    d = y - x
    sqrt_d = math.sqrt(d)
    result = 0
    if sqrt_d <= round(sqrt_d):
        result = int(round(sqrt_d)) * 2 - 1
    else:
        result = int(round(sqrt_d)) * 2

    sys.stdout.write(str(result)+'\n')

    T -= 1
