# Created by Jello on 2017. 7. 5.
import queue

V, E = map(int, str(input()).split(' '))
vertices = [[] for _ in range(V+1)]
visit = set()
bfs_queue = queue.Queue()
cnt = 0

for i in range(E):
    v1, v2 = map(int, str(input()).split(' '))
    vertices[v1].append(v2)
    vertices[v2].append(v1)

for i in range(1, len(vertices)):
    if i not in visit:
        bfs_queue.put(i)
        visit.add(i)
        cnt += 1
        while bfs_queue.qsize() > 0:
            e = bfs_queue.get()
            for j in vertices[e]:
                if j not in visit:
                    visit.add(j)
                    bfs_queue.put(j)
                    print('put {}'.format(j))

print(cnt)
