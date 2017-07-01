# Created by Jello on 2017. 7. 1.

a = int(input())
b = [1, 1]

for i in range(3, a+1):
    b.append(b[i-3]+b[i-2])

print(b[a-1])
