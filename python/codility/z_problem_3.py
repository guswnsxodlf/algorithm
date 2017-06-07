# Created by Jello on 2017. 6. 7.

def solution(A):
    A.sort()
    print(A)
    max_cnt = 1
    cnt = cnt_buff = 1

    for i in xrange(1, len(A)):
        if A[i] - A[i-1] > 1:
            cnt = cnt_buff = 1
        elif A[i] - A[i-1] == 1:
            cnt = cnt_buff + 1
            cnt_buff = 1
        else:
            cnt += 1
            cnt_buff += 1

        max_cnt = max(cnt, max_cnt)
        print('i:{} max:{} cnt:{} cnt_buff:{}'.format(i, max_cnt, cnt, cnt_buff))

    return max_cnt

print(solution([0]))
