import queue

MAX = 1000001
N, M, X = map(int, input().split(' '))
dist_come = [MAX] * (N+1)
dist_come[X] = 0
dist_leave = [MAX] * (N+1)
dist_leave[X] = 0
dist_sum = [0] * (N+1)

adjacency_list = [[] for x in range(N+1)]
adjacency_list_reverse = [[] for x in range(N+1)]

for i in range(M):
	s, e, w = map(int, input().split(' '))
	adjacency_list[s].append([w, e])
	adjacency_list_reverse[e].append([w, s])

q = queue.PriorityQueue()
for i in range(1, N+1):
	q.put([dist_come[i], i])

print('come')
while q.qsize() > 0:
	d = q.get()
	print(d)
	if d[0] <= dist_come[d[1]]:
		for i in adjacency_list[d[1]]:
			if i[0] + dist_come[d[1]] < dist_come[i[1]]:
				dist_come[i[1]] = i[0] + dist_come[d[1]]
				q.put([i[0] + dist_come[d[1]], i[1]])
				print('save', [i[0] + dist_come[d[1]], i[1]])

for i in range(1, N+1):
	q.put([dist_leave[i], i])

print('leave')
while q.qsize() > 0:
	d = q.get()
	print(d)
	if d[0] <= dist_leave[d[1]]:
		for i in adjacency_list_reverse[d[1]]:
			if i[0] + dist_leave[d[1]] < dist_leave[i[1]]:
				dist_leave[i[1]] = i[0] + dist_leave[d[1]]
				q.put([i[0] + dist_leave[d[1]], i[1]])
				print('save', [i[0] + dist_leave[d[1]], i[1]])

for i in range(1, N+1):
	dist_sum[i] = dist_leave[i] + dist_come[i]

print(max(dist_sum))
