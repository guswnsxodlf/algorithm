# Created by Jello on 2017. 9. 20.
import sys

def get_sum(n):
    if n <= N + 1:
        i = n-1
        return int(i * (i + 1) / 2)
    else:
        i = (2 * N) - n
        return int((N * (N - 1)) + N - (i * (i + 1) / 2))

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

n = 2
while get_sum(n) < K:
    n += 1

num_of_n = N - abs(N - (n - 1))
idx = (K - get_sum(n-1))

print(n, num_of_n, idx)

if n <= N + 1:
    i = ((idx-1) // 2) + 1
else:
    i = N - ((idx-1) // 2)

j = n - i
print(i, j)

sys.stdout.write(str(i * j))