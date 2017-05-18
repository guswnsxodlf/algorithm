# Created by Jello on 2017. 5. 18.

def solution(H):
    r = 1
    s = [H[0]]
    for v in H:
        if s[-1] > v:
            while True:
                s.pop()
                if len(s) < 1 or s[-1] <= v:
                    break
            if len(s) < 1 or s[-1] < v:
                s.append(v)
                r += 1
        elif s[-1] < v:
            s.append(v)
            r += 1
    return r
