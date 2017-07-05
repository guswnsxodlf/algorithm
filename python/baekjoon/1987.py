# Created by Jello on 2017. 7. 5.
def dfs(i, j):
    global count, max_count
    alphabet.add(board[i][j])
    count += 1
    max_count = max(max_count, count)
    print('Add {}, count={}, max_count={}'.format(board[i][j], count, max_count))

    if i > 0 and board[i-1][j] not in alphabet:
        dfs(i-1, j)
    if i < R-1 and board[i+1][j] not in alphabet:
        dfs(i+1, j)
    if j > 0 and board[i][j-1] not in alphabet:
        dfs(i, j-1)
    if j < C-1 and board[i][j+1] not in alphabet:
        dfs(i, j+1)

    alphabet.remove(board[i][j])
    count -= 1
    print('{} removed'.format(board[i][j]))


R, C = map(int, str(input()).split(' '))
board = [[] for x in range(R)]
alphabet = set()
count = max_count = 0

for i in range(R):
    board[i] = str(input())

# DFS
dfs(0, 0)

print(max_count)
