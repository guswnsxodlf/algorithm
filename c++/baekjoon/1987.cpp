#include <iostream>
#include <set>

using namespace std;
char board[20][20];
int cnt, max_cnt;
set<char> alphabet;
int R, C;

void dfs(int i, int j);

int main(){
    cnt = max_cnt = 0;
    cin >> R >> C;

    for(int i=0;i<R;i++){
        cin >> board[i];
    }

    dfs(0, 0);

    cout << max_cnt;
}

void dfs(int i, int j){
    alphabet.insert(board[i][j]);
    cnt++;
    if(max_cnt < cnt){
        max_cnt = cnt;
    }
    if(i > 0 && alphabet.find(board[i-1][j]) == alphabet.end()){
        dfs(i-1, j);
    }
    if(i < R-1 && alphabet.find(board[i+1][j]) == alphabet.end()){
        dfs(i+1, j);
    }
    if(j > 0 && alphabet.find(board[i][j-1]) == alphabet.end()){
        dfs(i, j-1);
    }
    if(j < C-1 && alphabet.find(board[i][j+1]) == alphabet.end()){
        dfs(i, j+1);
    }

    cnt--;
    alphabet.erase(alphabet.find(board[i][j]));
}
