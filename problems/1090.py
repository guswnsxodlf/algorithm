# Created by JHJ on 2016. 9. 3.

v1 = list(map(lambda a: int(a), str(input()).split(' ')))
print(pow(v1[1], (v1[2] - 1)) * v1[0])
