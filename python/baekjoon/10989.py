# Created by Jello on 2017. 9. 15.
import sys

MAX = 10001

N = int(sys.stdin.readline())
arr = [0] * MAX

for i in range(N):
    d = int(sys.stdin.readline())
    arr[d] += 1

for i in range(MAX):
	for j in range(arr[i]):
		print(i)