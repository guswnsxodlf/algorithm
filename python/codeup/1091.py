# Created by JHJ on 2016. 9. 5.


def compute(x, m, d, cnt):
	if cnt > 1:
		return compute((x * m) + d, m, d, cnt-1)
	else:
		return x

v1 = list(map(lambda x: int(x), str(input()).split(" ")))
print(compute(v1[0], v1[1], v1[2], v1[3]))
