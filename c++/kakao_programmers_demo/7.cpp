#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int dfs(const vector<string>& strs, const string& t, const string& cur_str, int cnt) {
	if (cur_str == t) {
		return cnt;
	}

	vector<int> result_arr;
	bool nothing = true;

	for (string s : strs) {
		bool checked = true;

		if (cur_str.length() + s.length() > t.length()) {
			checked = false;
		} else {
			for (int i=0;i<s.length();i++) {
				if (t[cur_str.length()+i] != s[i]) {
					checked = false;
					break;
				}
			}
		}

		if (checked) {
			nothing = false;
			result_arr.push_back(dfs(strs, t, cur_str+s, cnt+1));
		}
	}

	if (nothing) {
		return 20001;
	}

	int min_result = result_arr[0];
	for (int i=1;i<result_arr.size();i++) {
		min_result = min(min_result, result_arr[i]);
	}

	return min_result;
}

int solution(vector<string> strs, string t) {
	string s = "";
	int result = dfs(strs, t, s, 0);
	if (result == 20001) {
		result = -1;
	}
	return result;
}