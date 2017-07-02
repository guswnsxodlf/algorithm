# Created by Jello on 2017. 7. 2.

T = int(input())
while T > 0:
    # input
    LENGTH = int(input())
    upside = list(map(int, str(input()).split(' ')))
    downside = list(map(int, str(input()).split(' ')))
    stickers = [upside, downside]

    # init values
    dp = [[-1, -1] for i in range(LENGTH)]

    # set start value
    dp[0][0] = stickers[0][0]
    dp[0][1] = stickers[1][0]

    dp[1][0] = stickers[1][0] + stickers[0][1]
    dp[1][1] = stickers[0][0] + stickers[1][1]

    # dynamic programming
    for i in range(2, LENGTH):
        dp[i][0] = max(dp[i-2][1] + stickers[0][i], dp[i-1][1] + stickers[0][i])
        dp[i][1] = max(dp[i-2][0] + stickers[1][i], dp[i-1][0] + stickers[1][i])

    print(max(dp[LENGTH-1][0], dp[LENGTH-1][1]))

    T -= 1
