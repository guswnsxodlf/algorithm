#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#define MAX 10
using namespace std;
typedef pair< pair<int, int>, pair<int, int> > Path;
queue<Path> pathQ;
pair<int, int> red, blue, goal;
bool blueGoal = false, redGoal = false, finish = false, cantfinish = false;
Path finishNode;
map<Path, Path> searchedNodeMap;
map<Path, Path>::iterator mapIter;
void findGoal(vector< vector<char> >& field);
Path findFinalNode(vector< vector<char> >& field, Path p, char flag);
pair<int, int> findPosition(vector< vector<char> >& field, pair<int, int> n, char flag);
int findPath(vector< vector<char> >& field);
void searchNode(Path node, Path parent);
void checkFinish(Path p);
vector<bool> canMove(vector< vector<char> >& field, Path n);
int main() {
	int W, H;
	cin >> H >> W;
	vector< vector<char> > field(H, vector<char>(W));
	for(int i=0;i<H;i++){
		for(int j=0;j<W;j++){
			char fieldElement;
			cin >> fieldElement;
			field[i][j] = fieldElement;
			if(fieldElement == 'R'){
				red = make_pair(i, j);
			}else if(fieldElement == 'B'){
				blue = make_pair(i, j);
			}else if(fieldElement == 'O'){
				goal = make_pair(i, j);
			}
		}
	}
	Path init = make_pair(red, blue);
	searchNode(init, init);
	while(!finish && !cantfinish){
		findGoal(field);
	}
	if(cantfinish){
		cout << -1 << endl;
	}else{
		cout << findPath(field) << endl;
	}
	return 0;
}
void findGoal(vector< vector<char> >& field){
	if(pathQ.size() == 0){
		cantfinish = true;
		return;
	}
	Path pathPop = pathQ.front();
	vector<bool> direction = canMove(field, pathPop);
	if(direction[0]){
		Path n(findFinalNode(field, pathPop, 'U'));
		mapIter = searchedNodeMap.find(n);
		if(mapIter == searchedNodeMap.end()){
			checkFinish(n);
			if(!redGoal && !blueGoal){
				searchNode(n, pathPop);
			}else if(finish){
				searchNode(n, pathPop);
				return;
			}
		}
	}
	if(direction[1]){
		Path n(findFinalNode(field, pathPop, 'D'));
		mapIter = searchedNodeMap.find(n);
		if(mapIter == searchedNodeMap.end()){
			checkFinish(n);
			if(!redGoal && !blueGoal){
				searchNode(n, pathPop);
			}else if(finish){
				searchNode(n, pathPop);
				return;
			}
		}
	}
	if(direction[2]){
		Path n(findFinalNode(field, pathPop, 'L'));
		mapIter = searchedNodeMap.find(n);
		if(mapIter == searchedNodeMap.end()){
			checkFinish(n);
			if(!redGoal && !blueGoal){
				searchNode(n, pathPop);
			}else if(finish){
				searchNode(n, pathPop);
				return;
			}
		}
	}
	if(direction[3]){
		Path n(findFinalNode(field, pathPop, 'R'));
		mapIter = searchedNodeMap.find(n);
		if(mapIter == searchedNodeMap.end()){
			checkFinish(n);
			if(!redGoal && !blueGoal){
				searchNode(n, pathPop);
			}else if(finish){
				searchNode(n, pathPop);
				return;
			}
		}
	}
	pathQ.pop();
}
Path findFinalNode(vector< vector<char> >& field, Path p, char flag){
	Path originNode(p);
	Path n(findPosition(field, p.first, flag), findPosition(field, p.second, flag));
	if(n.first == n.second && n.first != goal){
		if(flag == 'U'){
			if(originNode.first.first > originNode.second.first){
				n.first.first++;
			}else{
				n.second.first++;
			}
		}else if(flag == 'D'){
			if(originNode.first.first > originNode.second.first){
				n.second.first--;
			}else{
				n.first.first--;
			}
		}else if(flag == 'L'){
			if(originNode.first.second > originNode.second.second){
				n.first.second++;
			}else{
				n.second.second++;
			}
		}else if(flag == 'R'){
			if(originNode.first.second > originNode.second.second){
				n.second.second--;
			}else{
				n.first.second--;
			}
		}
	}
	return n;
}
pair<int, int> findPosition(vector< vector<char> >& field, pair<int, int> n, char flag){
	while(true){
		pair<int, int> buffer(n);
		if(flag == 'U'){
			buffer.first--;
		}else if(flag == 'D'){
			buffer.first++;
		}else if(flag == 'L'){
			buffer.second--;
		}else if(flag == 'R'){
			buffer.second++;
		}
		if(field[buffer.first][buffer.second] == '#'){
			return n;
		}else if(field[buffer.first][buffer.second] == 'O'){
			return buffer;
		}else{
			n = buffer;
		}
	}
}
int findPath(vector< vector<char> >& field){
	int count = 0;
	Path n(finishNode);
	while(count++ < MAX){
		mapIter = searchedNodeMap.find(n);
		if(mapIter != searchedNodeMap.end()){
			if(mapIter->second == make_pair(red, blue)){
				break;
			}else{
				n = mapIter->second;
			}
		}
	}
	if(count > MAX){
		count = -1;
	}
	return count;
}
void searchNode(Path node, Path parent){
	pathQ.push(node);
	searchedNodeMap[node] = parent;
}
void checkFinish(Path p){
	redGoal = p.first == goal;
	blueGoal = p.second == goal;
	if(redGoal && !blueGoal){
		finishNode = p;
		finish = true;
	}
}
vector<bool> canMove(vector< vector<char> >& field, Path n){
	vector<bool> check(4, false);
	if(field[n.first.first-1][n.first.second] != '#' ||
		field[n.second.first-1][n.second.second] != '#'){
		check[0] = true;
	}
	if(field[n.first.first+1][n.first.second] != '#' ||
		field[n.second.first+1][n.second.second] != '#'){
		check[1] = true;
	}
	if(field[n.first.first][n.first.second-1] != '#' ||
		field[n.second.first][n.second.second-1] != '#'){
		check[2] = true;
	}
	if(field[n.first.first][n.first.second+1] != '#' ||
		field[n.second.first][n.second.second+1] != '#'){
		check[3] = true;
	}
	return check;
}
