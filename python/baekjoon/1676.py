N = int(input())
FIVE = 5
TWO = 2

f = FIVE
t = TWO
r = [0, 0] # [2 개수, 5 개수]

while t <= N:
	r[0] += N // t
	t *= TWO

while f <= N:
	r[1] += N // f
	f *= FIVE

print(min(r))