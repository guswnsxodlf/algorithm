# Created by JHJ on 2016. 9. 5.

students = [0] * 23

dummy = input()
v1 = list(map(lambda x: int(x), str(input()).split(" ")))

for i in v1:
	students[i-1] += 1

for i in students:
	print(i, end=' ')
