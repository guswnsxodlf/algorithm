# Created by Jello on 2017. 5. 18.

def solution(S):
    r = 1
    stack = []
    for v in S:
        if len(stack) >= 1 and (
                    [stack[-1], v] == ['{', '}'] or [stack[-1], v] == ['(', ')'] or [stack[-1], v] == ['[', ']']):
            stack.pop()
        else:
            stack.append(v)

    if len(stack) > 0:
        r = 0
    return r
