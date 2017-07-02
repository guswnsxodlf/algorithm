# Created by Jello on 2017. 7. 1.

T = int(input())

while T > 0:
    a = list(map(int, str(input()).split(' ')))
    m = z = 1
    for i in range(a[1]-a[0]+1, a[1]+1):
        z *= i
    for i in range(1, a[0]+1):
        m *= i

    print(z//m)
    T -= 1
