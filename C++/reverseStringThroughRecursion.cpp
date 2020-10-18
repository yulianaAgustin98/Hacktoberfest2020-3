/*
the reverse() function is called which is a recursive function. 
In the first function call, reverse() prints the last character of the string (numOfChars - 1), -1 
because array starts with 0. Then, substr() gives the string upto the 2nd last character, 
which is passed again to the reverse() function.

In the next reverse() call, the 2nd last character is printed because the 
string contains one less character from the last. After this, 
one character from the last is cut-off from the string again and passed to the reverse() function.

This goes until the length of the string equals 1, 
when the final character (or the first character) is printed and the loop ends.

*/

#include <iostream>
using namespace std;

void reverse(const string& a);

int main()
{
    string str;
    cout << " Please enter a string " << endl;
    getline(cin, str);
    reverse(str);
    return 0;    
}

void reverse(const string& str)
{
    size_t numOfChars = str.size();

    if(numOfChars == 1)
       cout << str << endl;
    else
    {
       cout << str[numOfChars - 1];
       reverse(str.substr(0, numOfChars - 1));
    }
}