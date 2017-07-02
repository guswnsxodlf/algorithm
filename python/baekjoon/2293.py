# Created by Jello on 2017. 7. 1.

T, M = list(map(int, str(input()).split(' ')))
coins = []
dp = [0] * (M+1)
dp[0] = 1
for i in range(T):
    coins.append(int(input()))

for c in coins:
    for j in range(c, M+1):
        dp[j] += dp[j - c]

print(dp[M])

