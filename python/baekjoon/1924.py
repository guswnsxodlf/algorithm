# Created by Jello on 2017. 6. 1.

a = list(map(int, str(input()).split(' ')))
sum_date = 0
for i in range(a[0]-1):
    if i+1 in [1,3,5,7,8,10,12]:
        sum_date += 31
    elif i+1 in [4,6,9,11]:
        sum_date += 30
    else:
        sum_date += 28

sum_date += a[1]

day = sum_date % 7

if day == 0:
    print('SUN')
elif day == 1:
    print('MON')
elif day == 2:
    print('TUE')
elif day == 3:
    print('WED')
elif day == 4:
    print('THU')
elif day == 5:
    print('FRI')
else:
    print('SAT')
