# Created by Jello on 2017. 9. 13.
import sys
import queue

def isValid(y, x):
    if y < 0 or x < 0 or y >= h or x >= w or visited[y][x] or m[y][x] == 0:
        return False
    return True

dx = [-1, 0, 1]
dy = [-1, 0, 1]

while True:
    w, h = map(int, sys.stdin.readline().strip().split(' '))

    if w == 0 and h == 0:
        break

    visited = [[False] * w for x in range(h)]
    m = []
    q = queue.Queue()
    island_cnt = 0

    for i in range(h):
        m.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and m[i][j] == 1:
                island_cnt += 1
                q.put([i, j])
                visited[i][j] = True

                # BFS
                while q.qsize() > 0:
                    d = q.get()
                    for k in dy:
                        for l in dx:
                            if k == 0 and l == 0:
                                continue
                            elif isValid(d[0] + k, d[1] + l):
                                q.put([d[0] + k, d[1] + l])
                                visited[d[0] + k][d[1] + l] = True

    print(island_cnt)
