#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int T;
	cin >> T;
	while(T--){
		int num, sum=0;
		cin >> num;

		int *r = new int[num];
		for(int i=0;i<num;i++){
			r[i] = true;
		}

		for(int i=1;i<num;i++){
			for(int j=i+1;j<=num;j+=(i+1)){
				r[j-1] = !r[j-1];
			}
		}

		for(int i=0;i<num;i++){
			if(r[i]){ sum++; }
		}

		cout << sum << endl;
	}
}