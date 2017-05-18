# Created by Jello on 2017. 5. 19.

def solution(A):
    candidate_cnt = 1
    candidate_ele = ''
    for v in A:
        if candidate_ele == v:
            candidate_cnt += 1
        else:
            candidate_cnt -= 1
            if candidate_cnt == 0:
                candidate_ele = v
                candidate_cnt = 1

    cnt = 0
    r = 0
    for i, v in enumerate(A):
        if v == candidate_ele:
            r = i
            cnt += 1

    if cnt <= len(A) / 2.0 or len(A) <= 0:
        return -1
    return r
