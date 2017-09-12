def dfs(strs, t, cur_str, cnt):
	# print('{}, {}'.format(cur_str, cnt))
	if cur_str == t:
		return cnt

	result_arr = []
	nothing = True

	for s in strs:
		checked = True

		if len(cur_str) + len(s) > len(t):
			checked = False
		else:
			for i in range(len(s)):
				if t[len(cur_str)+i] != s[i]:
					checked = False
					break

		if checked:
			nothing = False
			result_arr.append(dfs(strs, t, cur_str+s, cnt+1))

	if nothing:
		return 20001

	return min(result_arr)

def solution(strs, t):
	result = dfs(strs, t, '', 0)
	if result == 20001:
		result = -1
	return result

print(solution(['app','ap','p','l','e','ple','pp'], 'apple'))
print(solution(['ba','na','n','a'], 'banana'))
print(solution(['ba','an','nan','ban','n'], 'banana'))
print(solution(['a','an'], 'ana'))
