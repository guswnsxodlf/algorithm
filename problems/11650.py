# Created by JHJ on 2017.04.12
from operator import itemgetter

n = int(input())
points = []

for i in range(n):
    points.append(list(map(int, str(input()).split(' '))))

s = sorted(points, key=itemgetter(0, 1))

for i in s:
    print('{} {}'.format(i[0], i[1]))
