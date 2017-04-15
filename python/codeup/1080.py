# Created by JHJ on 2016. 9. 3.

v1 = int(input())
sum = 0

for i in range(1, 45):
	sum += i
	if sum >= v1:
		print(i)
		break
