# Created by Jello on 2017. 9. 14.
import sys

N = int(sys.stdin.readline())
arr = []
reverse_max_arr = [0] * N
reverse_max_value = 0
prev_value = 0
prev_state = False
result = 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print(arr)

for i in range(N):
    if i == 0:
        reverse_max_arr[-(i+1)] = arr[-(i+1)] + (i+1)
    else:
        reverse_max_arr[-(i+1)] = max(reverse_max_arr[-i], arr[-(i+1)] + (i+1))
print(reverse_max_arr)

for i in range(N):
    if arr[i] != prev_value:
        print('{} + {}'.format(arr[i], N))
        if arr[i] == arr[-1] or arr[i] + N >= reverse_max_arr[i+1]:
            result += 1
            prev_state = True
        else:
            prev_state = False

        prev_value = arr[i]

    else:
        print('prev_state: {}'.format(prev_state))
        if prev_state:
            result += 1

sys.stdout.write(str(result))
