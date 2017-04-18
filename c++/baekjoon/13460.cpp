#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

struct Node{
	pair<int, int> parent;
	char sign;
	bool touch;
};

struct Path{
	pair<int, int> red;
	pair<int, int> blue;
};

queue<Path> pathQ;
pair<int, int> red, blue, goal;
bool blueGoal = false, redGoal = false, finish = false, cantfinish = false;

void findGoal(vector< vector<Node> >& map);
Path findFinalNode(vector< vector<Node> >& map, Path p, char flag);
pair<int, int> findPosition(vector< vector<Node> >& map, pair<int, int> n, char flag);
int findPath(vector< vector<Node> >& map);
void searchNode(vector< vector<Node> >& map, Path node, pair<int, int> parent);
void checkFinish(Path p);

int main() {
	ifstream fileInput("input13460.txt");

	int W, H;

	fileInput >> H >> W;

	// Map
	vector< vector<Node> > map(H, vector<Node>(W));

	for(int i=0;i<H;i++){
		for(int j=0;j<W;j++){
			char mapElement;
			fileInput >> mapElement;
			map[i][j].sign = mapElement;
			map[i][j].touch = false;

			// Ball coordinate
			if(mapElement == 'R'){
				red = make_pair(i, j);
				map[i][j].touch = true;
			}else if(mapElement == 'B'){
				blue = make_pair(i, j);
			}else if(mapElement == 'O'){
				goal = make_pair(i, j);
			}
		}
	}

	// Queue initialize
	Path init = {red, blue};
	pathQ.push(init);

	// BFS
	while(!finish && !cantfinish){
		findGoal(map);
	}

	if(cantfinish){
		cout << -1 << endl;
	}else{
		cout << findPath(map) << endl;
	}

	return 0;
}

void findGoal(vector< vector<Node> >& map){
	if(pathQ.size() == 0){
		cout << "size 0" << endl;
		cantfinish = true;
		return;
	}

	Path pathPop = pathQ.front();

	if(pathPop.red == goal || pathPop.blue == goal){
		cout << "red goal or blue goal" << endl;
		pathQ.pop();
		return;
	}
	cout << pathPop.red.first << " " << pathPop.red.second << endl;

	if(map[pathPop.red.first-1][pathPop.red.second].sign == '.' ||
		map[pathPop.red.first-1][pathPop.red.second].sign == 'O' ||
		map[pathPop.red.first-1][pathPop.red.second].sign == 'B'){
		Path n(findFinalNode(map, pathPop, 'U'));
		if(!map[n.red.first][n.red.second].touch){
			cout << "U : push ("<< n.red.first << ", " << n.red.second << ")";
			cout << " ("<< n.blue.first << ", " << n.blue.second << ")" << endl;
			searchNode(map, n, pathPop.red);
		}
		checkFinish(n);
		if(finish){
			return;
		}
	}
	if(map[pathPop.red.first+1][pathPop.red.second].sign == '.' ||
		map[pathPop.red.first+1][pathPop.red.second].sign == 'O' ||
		map[pathPop.red.first+1][pathPop.red.second].sign == 'B'){
		Path n(findFinalNode(map, pathPop, 'D'));
		if(!map[n.red.first][n.red.second].touch){
			cout << "D : push ("<< n.red.first << ", " << n.red.second << ")";
			cout << " ("<< n.blue.first << ", " << n.blue.second << ")" << endl;
			searchNode(map, n, pathPop.red);
		}
		checkFinish(n);
		if(finish){
			return;
		}
	}
	if(map[pathPop.red.first][pathPop.red.second-1].sign == '.' ||
		map[pathPop.red.first][pathPop.red.second-1].sign == 'O' ||
		map[pathPop.red.first][pathPop.red.second-1].sign == 'B'){
		Path n(findFinalNode(map, pathPop, 'L'));
		if(!map[n.red.first][n.red.second].touch){
			cout << "L : push ("<< n.red.first << ", " << n.red.second << ")";
			cout << " ("<< n.blue.first << ", " << n.blue.second << ")" << endl;
			searchNode(map, n, pathPop.red);
		}
		checkFinish(n);
		if(finish){
			return;
		}
	}
	if(map[pathPop.red.first][pathPop.red.second+1].sign == '.' ||
		map[pathPop.red.first][pathPop.red.second+1].sign == 'O' ||
		map[pathPop.red.first][pathPop.red.second+1].sign == 'B'){
		Path n(findFinalNode(map, pathPop, 'R'));
		if(!map[n.red.first][n.red.second].touch){
			cout << "R : push ("<< n.red.first << ", " << n.red.second << ")";
			cout << " ("<< n.blue.first << ", " << n.blue.second << ")" << endl;
			searchNode(map, n, pathPop.red);
		}
		checkFinish(n);
		if(finish){
			return;
		}
	}
	pathQ.pop();
}

Path findFinalNode(vector< vector<Node> >& map, Path p, char flag){
	// flag U D L R
	pair<int, int> rOrigin(p.red);
	pair<int, int> bOrigin(p.blue);
	pair<int, int> r(findPosition(map, p.red, flag));
	pair<int, int> b(findPosition(map, p.blue, flag));

	// 겹쳤을 경우 처리
	if(r == b && r != goal){
		if(flag == 'U'){
			if(rOrigin.first > bOrigin.first){
				r.first++;
			}else{
				b.first++;
			}
		}else if(flag == 'D'){
			if(rOrigin.first > bOrigin.first){
				b.first--;
			}else{
				r.first--;
			}
		}else if(flag == 'L'){
			if(rOrigin.second > bOrigin.second){
				r.second++;
			}else{
				b.second++;
			}
		}else if(flag == 'R'){
			if(rOrigin.second > bOrigin.second){
				b.second--;
			}else{
				r.second--;
			}
		}
	}

	Path result = {r, b};
	return result;
}

pair<int, int> findPosition(vector< vector<Node> >& map, pair<int, int> n, char flag){
	// flag U D L R
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

		if(map[buffer.first][buffer.second].sign == '#'){
			return n;
		}else if(map[buffer.first][buffer.second].sign == 'O'){
			return buffer;
		}else{
			n = buffer;
		}
	}
}

int findPath(vector< vector<Node> >& map){
	int count = 0;
	while(true){
		count++;
		if(map[goal.first][goal.second].parent == red){
			break;
		}else{
			goal = map[goal.first][goal.second].parent;
		}
	}
	return count;
}

void searchNode(vector< vector<Node> >& map, Path node, pair<int, int> parent){
	pathQ.push(node);
	map[node.red.first][node.red.second].parent = parent;
	map[node.red.first][node.red.second].touch = true;
}

void checkFinish(Path p){
	if(p.red == goal){
		redGoal = true;
		cout << "Red Goal!" << endl;
	}else{
		redGoal = false;
	}

	if(p.blue == goal){
		blueGoal = true;
		cout << "Blue Goal!" << endl;
	}else{
		blueGoal = false;
	}

	if(redGoal && !blueGoal){
		finish = true;
	}
}
