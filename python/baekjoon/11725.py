# Created by Jello on 2017. 9. 12.
import queue

N = int(input())
adjacency_list = [[] for x in range(N)]
q = queue.Queue()
result = [0] * N

for i in range(N-1):
    n1, n2 = map(int, input().split(' '))
    adjacency_list[n1-1].append(n2)
    adjacency_list[n2-1].append(n1)

for i in adjacency_list[0]:
    q.put(i)
    result[i-1] = 1

while q.qsize() > 0:
    n = q.get()
    for i in adjacency_list[n-1]:
        if i != result[n-1]:
            q.put(i)
            result[i-1] = n

for i in range(1, len(result)):
    print(result[i])
