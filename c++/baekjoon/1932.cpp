#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int h, r = 0;
	cin >> h;

	int **map = new int*[h];
	int **cost = new int*[h];
	for(int i=0;i<h;i++){
		map[i] = new int[i+1];
		cost[i] = new int[i+1];

		for(int j=0;j<=i;j++){
			cin >> map[i][j];
		}
	}

	cost[0][0] = map[0][0];
	for(int i=1;i<h;i++){
		for(int j=0;j<=i;j++){
			if(j == 0){
				cost[i][j] = cost[i-1][j] + map[i][j];
			}else if(j == i){
				cost[i][j] = cost[i-1][j-1] + map[i][j];				
			}else{
				cost[i][j] = max(cost[i-1][j-1], cost[i-1][j]) + map[i][j];
			}
		}
	}

	r = cost[0][0];
	for(int i=1;i<h;i++){
		r = max(r, cost[h-1][i]);
	}

	cout << r << endl;
}