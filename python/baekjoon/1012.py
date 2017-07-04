# Created by Jello on 2017. 7. 5.
import queue

T = int(input())

while T > 0:
    M, N, K = map(int, str(input()).split(' '))
    bug = 0
    garden = [[0] * M for x in range(N)]
    bfs_queue = queue.Queue()
    
    for x in range(K):
        j, i = map(int, str(input()).split(' '))
        garden[i][j] = 1
    
    for i in range(N):
        for j in range(M):
            if garden[i][j] == 1:
                bug += 1
                bfs_queue.put([i, j])
                garden[i][j] = 2
                while bfs_queue.qsize() > 0:
                    k, l = bfs_queue.get()
                    if k > 0 and garden[k - 1][l] == 1:
                        garden[k - 1][l] = 2
                        bfs_queue.put([k - 1, l])
                    if k < N - 1 and garden[k + 1][l] == 1:
                        garden[k + 1][l] = 2
                        bfs_queue.put([k + 1, l])
                    if l > 0 and garden[k][l - 1] == 1:
                        garden[k][l - 1] = 2
                        bfs_queue.put([k, l - 1])
                    if l < M - 1 and garden[k][l + 1] == 1:
                        garden[k][l + 1] = 2
                        bfs_queue.put([k, l + 1])

    print(bug)

    T -= 1
