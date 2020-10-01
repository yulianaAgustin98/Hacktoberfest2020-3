#include<iostream>
using namespace std;
int main(){
  int n;
  cout<<"Enter your number :"<<endl;
  cin>>n;
  if(n % 2 == 0){
    cout<<"The entered number is even."<<endl;
  }else{
    cout<<"The entered number is odd."<<endl;
  }
}
