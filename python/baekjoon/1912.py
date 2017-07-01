# Created by Jello on 2017. 7. 1.

T = int(input())
seq = list(map(int, str(input()).split(' ')))
result = sum = seq[0]

for i in range(1, T):
    sum = max(sum+seq[i], seq[i])
    result = max(result, sum)

print(result)
