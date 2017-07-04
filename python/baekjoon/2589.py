# Created by Jello on 2017. 7. 5.
import queue

H, W = map(int, str(input()).split(' '))
m = [[] for x in range(H)]
visit = [[-1]*W for x in range(H)]
bfs_queue = queue.Queue()
distance = 0

for i in range(H):
    m[i] = str(input())

for i in range(H):
    for j in range(W):
        if m[i][j] == 'L':
            bfs_queue.put([i, j])
            visit[i][j] = 0
            while bfs_queue.qsize() > 0:
                i, j = bfs_queue.get()
                distance = max(distance, visit[i][j])
                if i > 0 and m[i - 1][j] == 'L' and visit[i - 1][j] == -1:
                    visit[i - 1][j] = visit[i][j] + 1
                    bfs_queue.put([i - 1, j])
                if i < H - 1 and m[i + 1][j] == 'L' and visit[i + 1][j] == -1:
                    visit[i + 1][j] = visit[i][j] + 1
                    bfs_queue.put([i + 1, j])
                if j > 0 and m[i][j - 1] == 'L' and visit[i][j - 1] == -1:
                    visit[i][j - 1] = visit[i][j] + 1
                    bfs_queue.put([i, j - 1])
                if j < W - 1 and m[i][j + 1] == 'L' and visit[i][j + 1] == -1:
                    visit[i][j + 1] = visit[i][j] + 1
                    bfs_queue.put([i, j + 1])

            visit = [[-1]*W for x in range(H)]

print(distance)
