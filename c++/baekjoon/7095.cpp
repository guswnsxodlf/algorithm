#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;

	double fac_log = log10(1.0);
	vector<int> arr;

	for(int i=1;fac_log<N;i++,fac_log+=log10(double(i))){
		cout << i << ' ' << fac_log << endl;
		if(fac_log+1 >= N && fac_log < N) {
			arr.push_back(i);
		}
	}

	if (arr.size() == 0){
		cout << "NO" << endl;
	} else {
		cout << arr.size() << endl;
		for(int i=0;i<arr.size();i++){
			cout << arr[i] << endl;
		}
	}
}