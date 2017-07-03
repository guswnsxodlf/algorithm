# Created by Jello on 2017. 7. 3.

L = int(input())
seq = list(map(int, str(input()).split(' ')))
dp_arr = [0] * L
max_length = result = 0

for i in range(L):
    for j in range(i):
        if seq[j] < seq[i]:
            max_length = max(dp_arr[j], max_length)
    dp_arr[i] = max_length+1
    max_length = 0
    result = max(result, dp_arr[i])

print(result)
