// Find the maximum amount that can be robbed if adjacent houses cannot be robbed

#include <bits/stdc++.h>
using namespace std;
int rob(int *arr, int n)
{
    if (n == 1)
    {
        return arr[0];
    }
    else if (n == 2)
    {
        return max(arr[0], arr[1]);
    }
    else
    {
        int dp[n];
        dp[0] = arr[0];
        dp[1] = max(arr[0], arr[1]);
        for (int i = 2; i < n; i++)
        {
            dp[i] = max(dp[i - 1], dp[i - 2]);
        }
        return dp[n - 1];
    }
}

int main()
{
    int arr[10];
    for (int i = 0; i < 10; i++)
        cin >> arr[i];
    rob(arr, 10);
}