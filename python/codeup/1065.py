# Created by JHJ on 2016. 9. 1.

v1 = str(input())
v1 = v1.split(" ")
for i in v1:
	if (int(i) % 2) == 0:
		print(int(i))
