# Created by Jello on 2017. 7. 4.
import queue


def bfs():
    # search
    e = bfs_queue.get()
    print(e, end=' ')

    # put into queue
    for i in range(1, len(vertices[e])):
        if vertices[e][i] == True and visit[i] == False:
            visit[i] = True
            bfs_queue.put(i)


def dfs(vertex):
    # search
    print(vertex, end=' ')

    # recursion
    for i in range(1, len(vertices[vertex])):
        if vertices[vertex][i] == True and visit[i] == False:
            visit[i] = True
            dfs(i)


bfs_queue = queue.Queue()
V, E, F = map(int, str(input()).split(' '))
vertices = [[False] * (V+1) for x in range(V+1)]
visit = [False] * (V+1)

for i in range(E):
    v1, v2 = map(int, str(input()).split(' '))
    vertices[v1][v2] = True
    vertices[v2][v1] = True

# DFS
visit[F] = True
dfs(F)

for i in range(1, V+1):
    visit[i] = False
print('')

# BFS
bfs_queue.put(F)
visit[F] = True
while bfs_queue.qsize() > 0:
    bfs()
