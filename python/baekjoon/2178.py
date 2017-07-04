# Created by Jello on 2017. 7. 4.
import queue

N, M = map(int, str(input()).split(' '))
maze = [[-1] * M for x in range(N)]
weight_map = [[-1] * M for x in range(N)]
bfs_queue = queue.Queue()

for i in range(N):
    maze[i] = list(map(int, str(input())))

weight_map[0][0] = 1
bfs_queue.put([0, 0])

while bfs_queue.qsize() > 0:
    i, j = bfs_queue.get()

    if i > 0 and maze[i-1][j] == 1 and weight_map[i-1][j] == -1:
        weight_map[i-1][j] = weight_map[i][j] + 1
        bfs_queue.put([i-1, j])
    if i < N-1 and maze[i+1][j] == 1 and weight_map[i+1][j] == -1:
        weight_map[i+1][j] = weight_map[i][j] + 1
        bfs_queue.put([i+1, j])
    if j > 0 and maze[i][j-1] == 1 and weight_map[i][j-1] == -1:
        weight_map[i][j-1] = weight_map[i][j] + 1
        bfs_queue.put([i, j-1])
    if j < M-1 and maze[i][j+1] == 1 and weight_map[i][j+1] == -1:
        weight_map[i][j+1] = weight_map[i][j] + 1
        bfs_queue.put([i, j+1])

    if weight_map[N-1][M-1] != -1:
        break

print(weight_map[N-1][M-1])
