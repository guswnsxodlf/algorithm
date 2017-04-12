# Created by Jello on 2017. 4. 12.

input1 = list(map(int, str(input()).split(' ')))
input2 = list(map(int, str(input()).split(' ')))

print(sorted(input2)[input1[1]-1])
