import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().strip().split(' ')))
state = [0] * N

for i in line:
	if i-1 == 0:
		state[i-1] = 1
	else:
		state[i-1] = state[i-2] + 1

print(N-max(state))
