arr = input()
open_arr = set(['(', '['])
close_arr = set([')', ']'])
st = []
score = [0] * 30
depth = 0

for i in range(len(arr)):
	if arr[i] in open_arr:
		st.append(arr[i])
		depth += 1
		print('push')
	elif arr[i] in close_arr:
		if i == 0:
			print('0')
			exit()
		else:
			if st[-1] == '(' and arr[i] == ')':
				st.pop()
				if score[depth+1] == 0:
					score[depth] += 2
				else:
					score[depth] += score[depth+1] * 2
				score[depth+1] = 0
				depth -= 1
			elif st[-1] == '[' and arr[i] == ']':
				st.pop()
				if score[depth+1] == 0:
					score[depth] += 3
				else:
					score[depth] += score[depth+1] * 3
				score[depth+1] = 0
				depth -= 1
			else:
				print('0')
				exit()
			print('pop')
			print(score)

print(score[1])