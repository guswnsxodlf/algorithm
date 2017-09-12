# Created by Jello on 2017. 9. 13.

N = int(input())
heights = list(map(int, input().strip().split(' ')))

h = 0
max_h = 0

for i in range(1, len(heights)):
    if heights[i] - heights[i-1] > 0:
        h += heights[i] - heights[i-1]
        max_h = max(max_h, h)
    else:
        h = 0

print(max_h)
