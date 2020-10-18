#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int t,n,k,l;
    cin>>t;
    for(int i=0;i<t;i++) {
        vector<int>ans;
        cin>>n>>k>>l;
        if(n>1 && k==1) {
            ans.push_back(-1);
        } else if(n==1) {
            ans.push_back(1);
        } else {
            if(k*l < n) {
                ans.push_back(-1);
            } else {
                int j=n;
                while(j>0) {
                    for(int v=1;v<=k;v++) {
                        if(j==0) break;
                        ans.push_back(v);
                        j--;
                    }
                    if(j==0) break;
                }
            }
        }
        for(int g=0;g<ans.size();g++) {
            cout<<ans[g]<<" ";
        }
        cout<<endl;
    }
    return 0;
}

