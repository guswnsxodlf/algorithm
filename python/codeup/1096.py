# Created by JHJ on 2016. 9. 5.

pan = []
for i in range(19):
	pan.append([0] * 19)
cnt = int(input())

for i in range(0, cnt):
	v1 = list(map(lambda x: int(x), str(input()).split(" ")))
	pan[v1[0] - 1][v1[1] - 1] += 1

for i in range(0, len(pan)):
	for j in pan[i]:
		print(j, end=' ')
	print()
