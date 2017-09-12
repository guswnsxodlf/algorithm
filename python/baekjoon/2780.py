T = int(input())
key_map = [
	[7],
	[2,4],
	[1,3,5],
	[2,6],
	[1,5,7],
	[2,4,6,8],
	[3,5,9],
	[4,8,0],
	[5,7,9],
	[6,8]
]

while T > 0:
	N = int(input())
	dp = [[1] * 10]

	for i in range(1, N):
		arr = []
		for j in range(10):
			sum = 0
			for k in key_map[j]:
				sum += (dp[i-1][k] % 1234567)

			arr.append(sum)

		dp.append(arr)

	sum = 0
	for i in range(10):
		sum += dp[-1][i]

	print(sum % 1234567)

	T -= 1
