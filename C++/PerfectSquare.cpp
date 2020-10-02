#include <bits/stdc++.h> 
using namespace std; 

bool check_PerfectSquare(int n ) { 
    float s=sqrt(n); 
    int a=s;
    if (a==s)
		return true;
    else 
		return false;
} 

int main() { 
  int n ;
  cout<<"Enter any number\n";
  cin>>n;
  if ( check_PerfectSquare(n)) 
    cout << "Yes"; 
  else
    cout << "No"; 
  return 0; 
} 
