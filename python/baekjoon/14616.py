# Created by Jello on 2017. 9. 14.
import sys
import bisect

def is_destroyed(r1, r2):
	r1_bs = bisect.bisect_left(laser, r1)
	r2_bs = bisect.bisect_left(laser, r2)

	if r1_bs != r2_bs:
		return True
	elif (r1_bs < len(laser) and r2_bs < len(laser)) and (laser[r1_bs] == r1 or laser[r2_bs] == r2):
		return True
	else:
		return False

def getTangent(x, y):
    return y/x

N = int(sys.stdin.readline())
radioactive = []
laser = []
cnt = 0

for i in range(N):
    data = list(map(int, sys.stdin.readline().strip().split(' ')))
    radioactive.append([getTangent(data[0], data[1]), getTangent(data[2], data[3])])
    print([getTangent(data[0], data[1]), getTangent(data[2], data[3])])

M = int(sys.stdin.readline())

for i in range(M):
    data = list(map(int, sys.stdin.readline().strip().split(' ')))
    laser.append(getTangent(data[0], data[1]))

laser.sort()

for i in range(N):
	print(radioactive[i][0], radioactive[i][1])
	if is_destroyed(radioactive[i][0], radioactive[i][1]):
		print('is_destroyed')
		cnt += 1

print(len(radioactive)-cnt)
