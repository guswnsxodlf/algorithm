# Created by Jello on 2017. 5. 22.

def solution(A):
    min = 200000
    max_profit = 0

    for v in A:
        if min > v:
            min = v
        else:
            if v - min > max_profit:
                max_profit = v - min

    return max_profit
