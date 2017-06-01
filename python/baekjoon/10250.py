# Created by Jello on 2017. 6. 1.
import math
T = int(input())
while T > 0:
    a = list(map(int, str(input()).split(' ')))
    if a[2]%a[0] == 0:
        h = a[0]
    else:
        h = a[2]%a[0]
    print('{}{:02d}'.format(h, int(math.ceil(a[2]/a[0]))))
    T -= 1
