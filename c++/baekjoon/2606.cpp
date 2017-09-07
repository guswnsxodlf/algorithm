#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
	int N_computers;
	int N_nodes;
	queue<int> q;
	cin >> N_computers;
	cin >> N_nodes;

	vector< vector<int> > adjacent(N_computers+1, vector<int>());
	vector<bool> isInfected(N_computers+1, false);

	for (int i=0;i<N_nodes;i++) {
		int n1, n2;
		cin >> n1 >> n2;
		adjacent[n1].push_back(n2);
		adjacent[n2].push_back(n1);
	}

	q.push(1);
	isInfected[1] = true;
	while (q.size() > 0) {
		int value = q.front();
		q.pop();
		
		for (int i=0;i<adjacent[value].size();i++) {
			if (!isInfected[adjacent[value][i]]){
				isInfected[adjacent[value][i]] = true;
				q.push(adjacent[value][i]);
			}
		}
	}

	int cnt = 0;
	for (int i=2;i<isInfected.size();i++) {
		if (isInfected[i]) {
			cnt++;
		}
	}

	cout << cnt;
}