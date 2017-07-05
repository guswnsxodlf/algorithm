# Created by Jello on 2017. 7. 6.

N = int(input())
MOD = 987654321

dp = [0] * (N+1)
dp[0] = 1
dp[2] = 1

for i in range(4, N+1, 2):
    for j in range(0, i, 2):
        dp[i] += (dp[j] * dp[i-2-j]) % MOD

print(dp[N] % MOD)
