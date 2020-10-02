#include <bits/stdc++.h>

using namespace std;
int lis(string s)
{
    vector<int> len(s.length());
    for (int k = 0; k < s.length(); k++)
    {
        len[k] = 1;
        for (int i = 0; i < k; i++)
        {
            if (s[k] > s[i])
            {
                len[k] = max(len[k], len[i] + 1);
            }
        }
    }
    return *max_element(len.begin(), len.end());
}
int main()
{
    string s;
    cin >> s;
    cout << lis(s) << endl;
}