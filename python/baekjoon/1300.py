# Created by Jello on 2017. 9. 20.
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

right = min(1000000000, N * N)
left = 1
mid = None

while True:
    mid = (right + left) // 2
    print(mid)
    cnt_upper = 0
    cnt_lower = 0
    for i in range(1, N+1):
        cnt_upper += min(mid // i, N)
        cnt_lower += min((mid-1) // i, N)

    print('cnt = {}, {}'.format(cnt_lower, cnt_upper))
    if cnt_lower < K <= cnt_upper:
        break
    elif cnt_upper < K:
        left = mid + 1
    elif cnt_lower >= K:
        right = mid - 1

sys.stdout.write(str(mid))
