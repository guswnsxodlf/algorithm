# Created by Jello on 2017. 7. 5.
import heapq, math

V = int(input())
E = int(input())

m = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2, w = map(int, str(input()).split(' '))
    m[v1].append([w, v2])

S, E = map(int, str(input()).split(' '))

p_queue = []
distance = [math.inf] * (V+1)

distance[S] = 0
heapq.heappush(p_queue, [0, S])
while len(p_queue) > 0:
    e = heapq.heappop(p_queue)[1]
    print('pop {}'.format(e))
    for w, v in m[e]:
        if distance[e] + w < distance[v]:
            distance[v] = distance[e] + w
            heapq.heappush(p_queue, [distance[v], v])
            print('push {}'.format(v))

print(distance[E])
