# Created by Jello on 2017. 9. 11.
def solution(v):
    x = {}
    y = {}
    result = []
    for i in v:
        x[i[0]] = not (i[0] in x)
        y[i[1]] = not (i[1] in y)

    for i in x:
        if x[i]:
            result.append(i)
    for i in y:
        if y[i]:
            result.append(i)

    return result
