# Created by Jello on 2017. 7. 1.

a = int(input())
b = [0, 1, 1]

for i in range(4, a+1):
    if i % 3 == 0:
        b.append(min(b[i-2]+1, b[(i-1)//3]+1))
    elif i % 2 == 0:
        b.append(min(b[i-2]+1, b[(i-1)//2]+1))
    else:
        b.append(b[i-2]+1)

print(b[a-1])
