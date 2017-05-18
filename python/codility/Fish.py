# Created by Jello on 2017. 5. 18.

def solution(A, B):
    stack = []
    for i in range(len(A)):
        if len(stack) > 0 and stack[-1]['d'] == 1 and B[i] == 0:
            if stack[-1]['s'] > A[i]:
                continue
            else:
                while True:
                    stack.pop()
                    if len(stack) > 0 and stack[-1]['s'] > A[i] and stack[-1]['d'] == 1:
                        break
                    elif len(stack) == 0 or stack[-1]['d'] == 0:
                        stack.append({'s': A[i], 'd': B[i]})
                        break
        else:
            stack.append({'s': A[i], 'd': B[i]})

    return len(stack)
