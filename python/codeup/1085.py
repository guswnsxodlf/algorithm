# Created by JHJ on 2016. 9. 3.

v1 = str(input()).split(" ")
mul = 1

for i in v1:
	mul *= int(i)

output = mul / (1024 * 1024 * 8.0)
print("{0:.1f} MB".format(output))
