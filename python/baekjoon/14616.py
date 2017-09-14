# Created by Jello on 2017. 9. 14.
import sys

def getTangent(x, y):
    return y/x

N = int(sys.stdin.readline())
radioactive = []
laser = []

for i in range(N):
    data = list(map(int, sys.stdin.readline().strip().split(' ')))
    data_arr = [getTangent(data[0], data[1]), getTangent(data[2], data[3])]
    radioactive.append([min(data_arr), max(data_arr)])

M = int(sys.stdin.readline())

for i in range(M):
    data = list(map(int, sys.stdin.readline().strip().split(' ')))
    laser.append(getTangent(data[0], data[1]))

