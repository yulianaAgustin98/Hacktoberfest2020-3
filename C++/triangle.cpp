#include <iostream>
using namespace std;

int left(){
for(int a = 0; a < 8; a++){
  for(int c = 1; c < a; c++){
    cout << "*";
  }
  cout << endl;
}
}

int right(){
cout << "**********";
for(int a = 0; a <= 8; a++){
cout << "*";
  for(int c = 8; c >= a; c--){
    cout << " ";
  }
  cout << "*" << endl;
}
cout << "*";

}

int main(){
cout << "#Hacktoberfest-2020" << endl;
cout << "[ Triangle C++ ]" << endl;
cout << "[1] left" << endl;
cout << "[2] right" << endl;
cout << "Choose one : ";
int user;
cin >> user;

if(user == 1){
left();
}else if(user == 2){
right();
}else{
cout << "Please choose between 1 and 2 !";
}

}
