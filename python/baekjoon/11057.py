# Created by Jello on 2017. 7. 3.

N = int(input())
dp = [[0] * 10 for x in range(N)]
sum_buff = result = 0

for i in range(N):
    if i == 0:
        for j in range(10):
            dp[i][j] = 1
    else:
        for j in range(10):
            sum_buff = 0
            for k in range(j+1):
                sum_buff += (dp[i-1][k] % 10007)
            dp[i][j] = sum_buff % 10007

for i in range(10):
    result += dp[N-1][i] % 10007

print(result % 10007)
