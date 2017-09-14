import sys
import queue

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def isValid(y, x):
	if y < 0 or x < 0 or y >= n or x >= m or visited[y][x]:
		return False
	return True


n, m = map(int, sys.stdin.readline().strip().split(' '))
visited = [[0] * m for i in range(n)]
maze = []
cnt = 0
q = queue.Queue()

for i in range(n):
	maze.append(sys.stdin.readline().strip())

q.put([0, 0])
visited[0][0] = 1
while q.qsize() > 0:
	d = q.get()
	if d[0] == n-1 and d[1] == m-1:
		break

	for i in range(len(dx)):
		if isValid(d[0]+dy[i], d[1]+dx[i]) and maze[d[0]+dy[i]][d[1]+dx[i]] == '1':
			q.put([d[0]+dy[i], d[1]+dx[i]])
			visited[d[0]+dy[i]][d[1]+dx[i]] = visited[d[0]][d[1]] + 1

print(visited[n-1][m-1])

