# Created by Jello on 2017. 5. 22.

a = list(map(int, str(input()).split(' ')))
print((a[0]+a[1])%a[2])
print(((a[0]%a[2])+(a[1]%a[2]))%a[2])
print((a[0]*a[1])%a[2])
print(((a[0]%a[2])*(a[1]%a[2]))%a[2])
