# Created by Jello on 2017. 7. 6.

N, M = map(int, str(input()).split(' '))
trees = list(map(int, str(input()).split(' ')))

left = 0
right = max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2
    sum = 0
    for t in trees:
        if t > mid:
            sum += t - mid

    if sum >= M:
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1

print(result)
