//Find number of ways to climb to stair if you can climb 1 or 2 at a time

#include <bits/stdc++.h>

using namespace std;

int solve(int n)
{
    int value[n + 1];
    value[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= 2; j++)
        {
            if (i - j > 0)
            {
                value[i] += value[i - j];
            }
        }
    }
    return value[n];
}

int main()
{
    int n;
    cin >> n;
    cout << solve(n);
}