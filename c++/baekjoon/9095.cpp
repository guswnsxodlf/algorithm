#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;

	while(T-- != 0){
		int num;
		cin >> num;

		int dp[11] = {};
		dp[0] = 1;

		for(int i=1;i<=num;i++){
			if(i-1 >= 0){
				dp[i] += dp[i-1];
			}
			if(i-2 >= 0){
				dp[i] += dp[i-2];
			}
			if(i-3 >= 0){
				dp[i] += dp[i-3];
			}
		}

		cout << dp[num] << endl;
	}
}