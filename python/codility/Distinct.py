def solution(A):
    cnt = {}
    for v in A:
        cnt[v] = True

    return len(cnt)
