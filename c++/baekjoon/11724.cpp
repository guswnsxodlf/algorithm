#include <iostream>
#include <queue>
#include <vector>
#include <list>
#include <set>
using namespace std;

int main(){
    int V, E, cnt=0;
    queue<int> bfs_queue;
    set<int> visit;


    cin >> V >> E;
    vector< list<int> > vertices(V+1);
    for(int i=1;i<=V;i++){
        list<int> l;
        vertices[i] = l;
    }

    for(int i=0;i<E;i++){
        int v1 = 0, v2 = 0;
        cin >> v1 >> v2;
        vertices[v1].push_back(v2);
        vertices[v2].push_back(v1);
    }

    for(int i=1;i<=V;i++){
        if(visit.find(i) == visit.end()){
            visit.insert(i);
            bfs_queue.push(i);
            cnt++;

            while(bfs_queue.size() > 0){
                int e = bfs_queue.front();
                bfs_queue.pop();

                for(list<int>::iterator j=vertices[e].begin();j!=vertices[e].end();j++){
                    if(visit.find(*j) == visit.end()){
                        bfs_queue.push(*j);
                        visit.insert(*j);
                    }
                }
            }
        }
    }

    cout << cnt;
}