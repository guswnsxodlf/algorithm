# Created by JHJ on 2016. 9. 1.

a = int(input())
divider = 10000
for i in range(0, 5):
	print("[{0}]".format((a//divider)*divider))
	a %= divider
	divider //= 10
