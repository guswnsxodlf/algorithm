(N, S) = list(map(int, input().strip().split(' ')))
arr = list(map(int, input().strip().split(' ')))
result_sum = 0
result_case = 0

for i in range(1, 2 ** N):
	result_sum = 0
	case_binary = bin(i)[2:].zfill(N)
	for j in range(N):
		if case_binary[j] == '1':
			result_sum += arr[j]
	if result_sum == S:
		result_case += 1

print(result_case)
