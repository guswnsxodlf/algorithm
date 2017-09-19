# Created by Jello on 2017. 9. 19.
import sys

def dfs(n, cnt):
    global max_length
    visited[n] = True
    has_node = False
    max_street = cnt
    sum_street_branch = 0

    for node, meter in adjacency_list[n]:
        if not visited[node]:
            has_node = True
            dfs_value = dfs(node, cnt + meter) + meter
            sum_street_branch += dfs_value - cnt
            print('{} {}'.format(dfs_value, sum_street_branch))

    if has_node:
        return sum_street_branch + cnt
    else:
        max_length = max(max_length, cnt)
        return cnt


N, S = map(int, sys.stdin.readline().strip().split(' '))
max_length = 0
adjacency_list = [[] for x in range(N+1)]
visited = [False] * (N+1)

for i in range(1, N):
    A, B, C = map(int, sys.stdin.readline().strip().split(' '))
    adjacency_list[A].append([B, C])
    adjacency_list[B].append([A, C])

sys.stdout.write(str(dfs(S, 0) - max_length))

