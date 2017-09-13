# Created by Jello on 2017. 9. 13.
import sys

N = int(sys.stdin.readline())
arr = []
dp = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in range(N):
    if i == 0:
        dp.append(arr[0])
    elif i == 1:
        dp.append(max(dp[0] + arr[i], dp[0] * arr[i]))
    else:
        dp.append(max(dp[i-2] + (arr[i-1] * arr[i]), dp[i-1] + arr[i]))

print(dp[-1])
