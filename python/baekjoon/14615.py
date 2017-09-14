# Created by Jello on 2017. 9. 15.
import sys
import queue

SUCCESS = 'Defend the CTP\n'
FAIL = 'Destroyed the CTP\n'

def bfs(initial, state, graph_list):
    q = queue.Queue()
    searched = [False] * (N + 1)

    q.put(initial)
    searched[initial] = True

    while q.qsize() > 0:
        d = q.get()
        for i in graph_list[d]:
            if not searched[i]:
                q.put(i)
                searched[i] = True
                state[i] = True

N, M = map(int, sys.stdin.readline().split(' '))
adjacency_list = [[] for i in range(N+1)]
adjacency_list_reverse = [[] for i in range(N+1)]
connected_with_last_islands = {}
connected_with_first_islands = {}

for i in range(M):
    X, Y = map(int, sys.stdin.readline().split(' '))
    adjacency_list[X].append(Y)
    adjacency_list_reverse[Y].append(X)

bfs(1, connected_with_first_islands, adjacency_list)
bfs(N, connected_with_last_islands, adjacency_list_reverse)

T = int(sys.stdin.readline())

while T > 0:
    C = int(sys.stdin.readline())
    if C in connected_with_last_islands and C in connected_with_first_islands:
        sys.stdout.write(SUCCESS)
    else:
        sys.stdout.write(FAIL)

    T -= 1
