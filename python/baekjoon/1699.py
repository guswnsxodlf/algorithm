# Created by Jello on 2017. 7. 3.

N = int(input())
dp = [100001] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    if i == 1:
        dp[i] = 1
    else:
        j = 1
        while i-(j*j) >= 0:
            dp[i] = min(dp[i], dp[i-(j*j)] + 1)
            j += 1

print(dp[N])
