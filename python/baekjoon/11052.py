# Created by Jello on 2017. 7. 2.

B = int(input())
price = [0] + list(map(int, str(input()).split(' ')))
dp = [-1] * (B+1)
dp[0] = 0

for i in range(1, B+1):
    for j in range(i+1):
        dp[i] = max(dp[i], dp[i-j] + price[j])

print(dp[B])
