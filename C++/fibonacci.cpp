#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[]) {
    int n;
    cout << "Enter the number of terms to print: ";
    cin >> n;
    long long a, b, c;
    a = 0;
    b = 1;
    n -= 2;
    cout << a << " " << b << " ";
    while(n--) {
        c = a + b;
        cout << c << " ";
        a = b;
        b = c;
    }
    cout << endl;
    
    return 0;
}
