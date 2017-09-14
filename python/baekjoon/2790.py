# Created by Jello on 2017. 9. 14.
import sys

N = int(sys.stdin.readline())
arr = []
max_cnt = 0
max_score = 0
result = 0

for i in range(N):
    data = int(sys.stdin.readline())
    arr.append(data)
    if max_score == data:
        max_cnt += 1
    elif data > max_score:
        max_score = data
        max_cnt = 1

print(max_score, max_cnt)

for n in arr:
    if n + N >= max_score + max_cnt:
        result += 1

print(result)
