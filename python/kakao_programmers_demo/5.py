# Created by Jello on 2017. 9. 12.

def solution(land):
    result = [land[0], ]
    for i in range(1, len(land)):

        # for 문으로 바꾸면 좋을듯
        arr = []
        arr.append(max(result[i-1][1], result[i-1][2], result[i-1][3]) + land[i][0])
        arr.append(max(result[i-1][0], result[i-1][2], result[i-1][3]) + land[i][1])
        arr.append(max(result[i-1][0], result[i-1][1], result[i-1][3]) + land[i][2])
        arr.append(max(result[i-1][0], result[i-1][1], result[i-1][2]) + land[i][3])
        result.append(arr)

    return max(result[-1])

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))