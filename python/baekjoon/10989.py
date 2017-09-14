# Created by Jello on 2017. 9. 15.
import sys

MAX = 10000

N = int(sys.stdin.readline())
arr_map = {}

for i in range(N):
    d = int(sys.stdin.readline())
    if d in arr_map:
        arr_map[d] += 1
    else:
        arr_map[d] = 1

for i in range(MAX+1):
    if i in arr_map:
        for j in range(arr_map[i]):
            print(i)
