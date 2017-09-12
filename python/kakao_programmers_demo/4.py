# Created by Jello on 2017. 9. 11.
# 해결 안됨


# 특정 점에서 우측 하단으로 정사각형 최대 길이 측정
def find_length(board, i, j):
    length = 0

    # i, j를 기준으로 우측 하단으로 넓혀나가면서 검사
    while True:
        checked = True

        # 길이 넘어가면 break
        if i + length >= len(board) or j + length >= len(board[0]):
            break

        for k in range(i, i + length + 1):
            print('{}, {}를 검사합니다 {}'.format(k, j+length, board[k][j+length]))
            if board[k][j + length] == 0:
                # 0 발견되면 break
                checked = False
                break

        if not checked:
            break

        for l in range(j, j + length):
            print('{}, {}를 검사합니다 {}'.format(i+length, l, board[i+length][l]))
            if board[i + length][l] == 0:
                # 0 발견되면 break
                checked = False
                break

        if not checked:
            break

        length += 1

    print('{} 리턴합니다'.format(length))
    return length


def solution(board):
    result_max = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if len(board) - i <= result_max or len(board[0]) - j <= result_max:
                break
            else:
                print('{}, {} 기준점으로 시작합니다'.format(i, j))
                result_max = max(result_max, find_length(board, i, j))

    return result_max ** 2

print(solution([[0,0,1,1],[1,1,1,1]]))