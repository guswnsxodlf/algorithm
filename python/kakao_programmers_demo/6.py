# Created by Jello on 2017. 9. 12.
# 해결 안됨

def get(arr, s, e):
    length = e-s
    if length <= 2:
        return max(arr[s], arr[e-1])
    elif length == 3:
        return max(arr[s]+arr[e-1], arr[s+1])
    else:
        return max(arr[s]+get(arr, s+2, e), arr[s+1]+get(arr, s+3, e))

def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    else:
        return max(sticker[0]+get(sticker, 2, len(sticker)-1), sticker[1]+get(sticker, 3, len(sticker)))


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1,3,2,1]))
