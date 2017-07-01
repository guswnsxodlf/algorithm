# Created by Jello on 2017. 7. 1.

a = int(input())
dp = [1, 2]

for i in range(2, a):
    dp.append(dp[i-1]+dp[i-2])

print(dp[a-1]%10007)
