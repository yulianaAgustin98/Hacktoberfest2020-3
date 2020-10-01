#include<bits/stdc++.h>
using namespace std;

int main(){
    vector <int> a;
    int k;
    for(int i = 0 ; i < 5 ;i++){
        cin >> k;
        a.push_back(k);
    }
    cin >> k;
    priority_queue<int , vector<int> ,greater<>> pq;
    for(int i = 0; i < k ; i++) pq.push(a[i]);
    for(int i = k ; i < 5 ;i++){
        if(a[i] > pq.top()){
            pq.pop();
            pq.push(a[i]);
        }
    }
    cout << pq.top() << endl;;
}