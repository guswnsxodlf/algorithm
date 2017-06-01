# Created by Jello on 2017. 6. 1.

a = int(input())

numerator = denominator = 1

down = False

for i in range(a-1):
    if not down:
        if numerator == 1:
            denominator += 1
            down = True
        else:
            numerator -= 1
            denominator += 1
    else:
        if denominator == 1:
            numerator += 1
            down = False
        else:
            denominator -= 1
            numerator += 1

print('{}/{}'.format(numerator, denominator))
