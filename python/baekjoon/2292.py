# Created by Jello on 2017. 5. 22.
import math
a = int(input())

cal = math.ceil((a-1)/6)
i = 1
sum_i = 0
while True:
    if cal <= sum_i:
        break
    sum_i += i
    i += 1

print(i)
