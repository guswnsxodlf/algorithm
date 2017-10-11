import time
N = int(input())

cnt = 0
t = N
while True:
	cnt += 1
	t = ((t % 10) * 10) + (((t % 10) + (t // 10)) % 10)
	print(t)
	time.sleep(1)
	if t == N:
		break

print(cnt)