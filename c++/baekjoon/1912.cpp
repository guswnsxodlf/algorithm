#include <iostream>
#include <vector>
using namespace std;

int main(){
    int T = 0;
    cin >> T;
    vector<int> arr(T);
    int sum, result;
    sum = result = 0;

    for(int i=0;i<T;i++){
        cin >> arr[i];
        if(i == 0) sum = result = arr[i];
        else{
            sum = sum+arr[i] > arr[i] ? sum+arr[i] : arr[i];
            result = result > sum ? result : sum;
        }
    }

    cout << result;
}