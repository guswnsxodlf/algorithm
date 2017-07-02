# Created by Jello on 2017. 7. 2.

L = int(input())

dp = [-1] * L

for i in range(L):
    if i == 0:
        dp[0] = 1
    elif i == 1:
        dp[1] = 3
    else:
        dp[i] = (dp[i-1] + (dp[i-2]*2)) % 10007

print(dp[L-1])
