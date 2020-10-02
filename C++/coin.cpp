//Given an array of coins select minimum number of coins to form the sum n
//O(nk) where n is given sum and k is the number of elements in the coin array

#include <bits/stdc++.h>

using namespace std;

int arr[3] = {1, 2, 3};
int min(int a, int b)
{
    return a > b ? b : a;
}

int solve(int x)
{
    int value[x + 1];
    value[0] = 0;
    int first[x];
    for (int i = 1; i <= x; i++)
    {
        value[i] = INT_MAX;
        for (auto c : arr)
        {
            if (i - c >= 0)
            {
                value[i] = min(value[i], value[i - c] + 1);
                // first[i] = c;
            }
        }
    }
    // for(int i = 1; i < value[x] ; i++) cout << first[i] << endl;
    return value[x];
}
int main()
{
    int n = 9;
    cout << solve(n);
}