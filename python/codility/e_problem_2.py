# Created by Jello on 2017. 6. 14.

m_map = {
    'January': 0,
    'February': 1,
    'March': 2,
    'April': 3,
    'May': 4,
    'June': 5,
    'July': 6,
    'August': 7,
    'September': 8,
    'October': 9,
    'November': 10,
    'December': 11
}
d_map = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}


def get_end_day(Y, M):
    if M in [0, 2, 4, 6, 7, 9, 11]:
        return 31
    elif M in [3, 5, 8, 10]:
        return 30
    else:
        if Y % 4 == 0:
            return 29
        else:
            return 28


def day_to_date(D, W):
    d = W + (D % 7) - 1
    if d == -1:
        d = 6
    elif d > 6:
        d -= 7

    return d


def get_day(Y, M, D):
    r = 0
    for i in xrange(m_map[M]):
        r += get_end_day(Y, i)

    r += D

    return r


def solution(Y, A, B, W):
    start = get_day(Y, A, 1)
    end = get_day(Y, B, get_end_day(Y, m_map[B]))

    while True:
        if day_to_date(start, d_map[W]) == 0:
            break
        else:
            start += 1

    while True:
        if day_to_date(end, d_map[W]) == 6:
            break
        else:
            end -= 1
    print(start, end)
    return ((end + 1) - start) // 7
