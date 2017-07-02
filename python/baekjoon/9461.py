# Created by Jello on 2017. 7. 3.

T = int(input())

while T > 0:
    N = int(input())

    dp = [-1] * N

    for i in range(N):
        if i <= 2:
            dp[i] = 1
        elif 2 < i <= 4:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-5]

    print(dp[N-1])

    T -= 1
