# Created by JHJ on 2016. 9. 3.

v1 = int(input())
sum = 0
for i in range(0, v1+1):
	if (i % 2) == 0:
		sum += i

print(sum)