def solution(A):
    zero = []
    num_of_case = 0
    for i, v in enumerate(A):
        if v == 0:
            zero.append(i)

    for i, v in enumerate(zero):
        num_of_case += (len(A) - (v + 1)) - (len(zero) - (i + 1))
        if num_of_case > 1000000000:
            return -1

    return num_of_case
