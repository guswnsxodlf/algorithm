# Created by Jello on 2017. 9. 20.
import sys

def dp_func(arr):
    dp = [0] * len(arr)
    for j in range(len(arr)):
        if j == 0:
            dp[j] = arr[j]
        elif j == 1:
            dp[j] = max(arr[j], arr[j-1])
        else:
            dp[j] = max(dp[j-2] + arr[j], dp[j-1])
    return dp[-1]

while True:
    M, N = map(int, sys.stdin.readline().strip().split(' '))

    if (M, N) == (0, 0):
        break

    arr = [0] * M
    dp = [0] * M

    for i in range(M):
        arr_sub = list(map(int, sys.stdin.readline().strip().split(' ')))
        arr[i] = dp_func(arr_sub)

    sys.stdout.write(str(dp_func(arr))+'\n')
    sys.stdout.flush()
