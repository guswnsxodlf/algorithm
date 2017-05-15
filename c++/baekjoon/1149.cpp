#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin >> T;

	int **data = new int*[T];
	int **cost = new int*[T];

	for(int i=0;i<T;i++){
		data[i] = new int[3];
		cin >> data[i][0] >> data[i][1] >> data[i][2];
	}

	cost[0] = new int[3];
	cost[0][0] = data[0][0];
	cost[0][1] = data[0][1];
	cost[0][2] = data[0][2];

	for(int i=1;i<T;i++){
		cost[i] = new int[3];
		cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + data[i][0];
		cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + data[i][1];
		cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + data[i][2];
	}

	cout << min(min(cost[T-1][0], cost[T-1][1]), cost[T-1][2]);
}