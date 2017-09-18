# Created by Jello on 2017. 9. 19.
import sys
import math

N, M = map(int, sys.stdin.readline().split(' '))
P = list(map(int, sys.stdin.readline().split(' ')))
train_pass_cnt_state = [0] * (N+1)
train_pass_cnt = [0, ]
costs = [[],]
efficient_cnt = [0, ]
result = 0

for i in range(N-1):
    data = list(map(int, sys.stdin.readline().split(' ')))
    costs.append(data)
    efficient_cnt.append(int(math.ceil(data[2] / (data[0] - data[1]))))
print(costs)
print(efficient_cnt)

for i in range(len(P)-1):
    less = min(P[i], P[i+1])
    bigger = max(P[i], P[i+1])
    train_pass_cnt_state[less] += 1
    train_pass_cnt_state[bigger] -= 1
print(train_pass_cnt_state)

for i in range(1, len(train_pass_cnt_state)-1):
    train_pass_cnt.append(train_pass_cnt[-1] + train_pass_cnt_state[i])
    if train_pass_cnt[i] >= efficient_cnt[i]:
        result += costs[i][2] + (costs[i][1] * train_pass_cnt[i])
    else:
        result += costs[i][0] * train_pass_cnt[i]
print(train_pass_cnt)

sys.stdout.write(str(result))
