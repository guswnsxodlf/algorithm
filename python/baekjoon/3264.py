# Created by Jello on 2017. 9. 19.
import sys

def dfs(n, cnt):
    visited[n] = True
    has_node = False
    max_street = cnt
    sum_street_branch = 0

    for node, meter in adjacency_list[n]:
        if not visited[node]:
            has_node = True
            dfs_value = dfs(node, cnt + meter)
            max_street = max(max_street, dfs_value)
            sum_street_branch += dfs_value - cnt

    if has_node:
        return max_street + ((sum_street_branch - (max_street - cnt)) * 2)
    else:
        return cnt


N, S = map(int, sys.stdin.readline().strip().split(' '))
adjacency_list = [[] for x in range(N+1)]
visited = [False] * (N+1)

for i in range(1, N):
    A, B, C = map(int, sys.stdin.readline().strip().split(' '))
    adjacency_list[A].append([B, C])
    adjacency_list[B].append([A, C])

sys.stdout.write(str(dfs(S, 0)))

