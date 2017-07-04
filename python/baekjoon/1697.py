# Created by Jello on 2017. 7. 4.
import queue

N, K = map(int, str(input()).split(' '))
MAX = 200000
m = [-1] * MAX
bfs_queue = queue.Queue()

m[N] = 0
bfs_queue.put(N)

while m[K] == -1:
    i = bfs_queue.get()

    if i > 0 and m[i-1] == -1:
        m[i-1] = m[i] + 1
        bfs_queue.put(i-1)
    if i < MAX-1 and m[i+1] == -1:
        m[i+1] = m[i] + 1
        bfs_queue.put(i+1)
    if i < 100000 and m[i*2] == -1:
        m[i*2] = m[i] + 1
        bfs_queue.put(i*2)

print(m[K])
