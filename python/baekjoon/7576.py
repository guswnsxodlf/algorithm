# Created by Jello on 2017. 7. 4.
M, N = map(int, str(input()).split(' '))
tomatoes = [[] for x in range(N)]
stack = []
buffered_stack = []
is_all_ripe = True
day = 0

for i in range(N):
    tomatoes[i] = list(map(int, str(input()).split(' ')))
    for j in range(M):
        if tomatoes[i][j] == 1:
            stack.append([i, j])
        elif tomatoes[i][j] == 0:
            is_all_ripe = False

if is_all_ripe:
    print('0')
    exit()

while len(stack) > 0:
    while len(stack) > 0:
        i, j = stack.pop()
        print('{}, {} search'.format(i, j))

        if i > 0 and tomatoes[i - 1][j] == 0:
            tomatoes[i - 1][j] = 1
            buffered_stack.append([i - 1, j])
            print('{}, {} put'.format(i - 1, j))
        elif i < N - 1 and tomatoes[i + 1][j] == 0:
            tomatoes[i + 1][j] = 1
            buffered_stack.append([i + 1, j])
            print('{}, {} put'.format(i + 1, j))

        if j > 0 and tomatoes[i][j - 1] == 0:
            tomatoes[i][j - 1] = 1
            buffered_stack.append([i, j - 1])
            print('{}, {} put'.format(i, j - 1))
        elif j < M - 1 and tomatoes[i][j + 1] == 0:
            tomatoes[i][j + 1] = 1
            buffered_stack.append([i, j + 1])
            print('{}, {} put'.format(i, j + 1))

    stack = buffered_stack
    buffered_stack = []
    day += 1
    print('day {}'.format(day))

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            print('-1')
            exit()

print(day-1)
