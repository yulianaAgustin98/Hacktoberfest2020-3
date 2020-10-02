//Given a coin array find all possible ways to get x as the sum

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int arr[] = {2, 3, 5, 6};
    int x = 10;
    vector<int> value(x, 0);
    value[0] = 1;

    for (int i = 1; i <= x; i++)
    {
        for (auto c : arr)
        {
            if (i - c >= 0)
            {
                value[i] += value[i - c];
            }
        }
    }
    cout << value[x] << endl;
}