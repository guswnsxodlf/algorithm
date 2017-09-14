# Created by Jello on 2017. 9. 15.
import sys

def ms(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = ms(arr[:mid])
    right = ms(arr[mid:])

    left_idx = 0
    right_idx = 0
    result = []

    while right_idx < len(right) or left_idx < len(left):
        if right_idx >= len(right):
            result.append(left[left_idx])
            left_idx += 1
        elif left_idx >= len(left):
            result.append(right[right_idx])
            right_idx += 1
        elif left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    return result


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

for i in ms(arr):
    print(i)
