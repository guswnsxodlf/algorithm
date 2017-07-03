# Created by Jello on 2017. 7. 3.

N = int(input())
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = 3
    elif i % 2 == 0:
        dp[i] = 0
    else:
        dp[i] = dp[i-2]*3
        for j in range(-1, i-4+1, 2):
            if j == -1:
                dp[i] += 2
            else:
                dp[i] += dp[j]*2

print(dp[N-1])
