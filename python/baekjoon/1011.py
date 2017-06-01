# Created by Jello on 2017. 6. 1.
import math
T = int(input())
while T > 0:
    a = list(map(int, str(input()).split(' ')))
    d = a[1] - a[0]
    round_root_d = round(math.sqrt(d))
    if pow(round_root_d, 2) < d:
        print(round_root_d*2)
    else:
        print((round_root_d*2)-1)
    T -= 1
