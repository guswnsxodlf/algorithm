# Created by Jello on 2017. 7. 1.

L = int(input())
MOD = 1000000000
dp = [[0]*10 for x in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, L+1):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i-1][1] % MOD
        elif j == 9:
            dp[i][9] = dp[i-1][8] % MOD
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % MOD

print(sum(dp[L]) % MOD)
