# Created by Jello on 2017. 5. 18.

def solution(A):
    r = 0
    candidate_ele = ''
    candidate_cnt = 1
    for v in A:
        if candidate_ele == v:
            candidate_cnt += 1
        else:
            candidate_cnt -= 1
            if candidate_cnt <= 0:
                candidate_ele = v
                candidate_cnt = 1

    cnt = 0
    sum_cnt = [0] * len(A)
    for i, v in enumerate(A):
        if candidate_ele == v:
            cnt += 1
        sum_cnt[i] = cnt

    if cnt <= len(A) / 2.0:
        return 0

    for i, v in enumerate(sum_cnt):
        if (i + 1) / 2.0 < v and (len(sum_cnt) - (i + 1)) / 2.0 < sum_cnt[-1] - v:
            r += 1

    return r
