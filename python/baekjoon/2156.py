# Created by Jello on 2017. 7. 1.

T = int(input())
wine = []
dp = []
for i in range(T):
    wine.append(int(input()))
    if i == 0:
        dp.append(wine[0])
    elif i == 1:
        dp.append(wine[1] + wine[0])
    elif i == 2:
        dp.append(max(wine[0]+wine[1], wine[1]+wine[2], wine[0]+wine[2]))
    else:
        dp.append(max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1]))

print(dp[T-1])
