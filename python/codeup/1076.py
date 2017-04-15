# Created by JHJ on 2016. 9. 3.

v1 = str(input())

for i in range(ord('a'), ord(v1)+1):
	print(chr(i), end='')
	if i != ord(v1):
		print(' ', end='')
