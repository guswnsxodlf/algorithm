# Created by Jello on 2017. 7. 3.

N, K = map(int, str(input()).split(' '))
MAX = 10001
coins = []
dp = [MAX] * (K+1)
dp[0] = 0
for i in range(N):
    coins.append(int(input()))

for i in range(1, K+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin]+1)

r = dp[K]
if r == MAX:
    print(-1)
else:
    print(dp[K])
