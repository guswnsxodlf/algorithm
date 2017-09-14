import sys

def getPrimeFactor(N):
	FIVE = 5
	TWO = 2

	f = FIVE
	t = TWO
	r = [0, 0]

	while t <= N:
		r[0] += N // t
		t *= TWO

	while f <= N:
		r[1] += N // f
		f *= FIVE

	return r

n, m = map(int, sys.stdin.readline().strip().split(' '))

n1 = getPrimeFactor(n)
n2 = getPrimeFactor(n-m)
d = getPrimeFactor(m)

print(min([n1[0]-n2[0]-d[0], n1[1]-n2[1]-d[1]]))



