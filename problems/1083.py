# Created by JHJ on 2016. 9. 3.

v1 = int(input())

for i in range(1, v1+1):
	if (i % 3) == 0:
		print('X', end=' ')
	else:
		print(i, end=' ')
