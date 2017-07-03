# Created by Jello on 2017. 7. 3.

N, M = map(int, str(input()).split(' '))
candy_map = [0] * (N+1)
dp = [0] * (N+1)

for i in range(N+1):
    if i == 0:
        candy_map[0] = [0] * (M+1)
    else:
        candy_map[i] = [0] + list(map(int, str(input()).split(' ')))

    dp[i] = [0] * (M+1)

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + candy_map[i][j]

print(dp[N][M])

