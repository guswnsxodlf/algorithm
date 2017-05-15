#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int dp[1000001];
	int num, cnt=0;
	cin >> num;

	dp[1] = 0;
	for(int i=2;i<=num;i++){
		if(i % 2 == 0 && i % 3 == 0){
			dp[i] = min(min(dp[i/2], dp[i/3]), dp[i-1]) + 1;
		}else if(i % 2 == 0){
			dp[i] = min(dp[i/2], dp[i-1]) + 1;
		}else if(i % 3 == 0){
			dp[i] = min(dp[i/3], dp[i-1]) + 1;
		}else{
			dp[i] = dp[i-1] + 1;
		}
	}

	cout << dp[num];
}