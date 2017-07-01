# Created by Jello on 2017. 7. 1.

a = int(input())
stairs = []
dp = []

for i in range(a):
    stairs.append(int(input()))
    if i == 0 :
        dp.append(stairs[0])
    elif i == 1:
        dp.append(stairs[0] + stairs[1])
    elif i == 2:
        dp.append(max(stairs[1] + stairs[2], stairs[0] + stairs[2]))
    else:
        dp.append(max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i]))

print(dp[a-1])
