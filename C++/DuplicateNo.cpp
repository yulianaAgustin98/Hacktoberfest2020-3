/*
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
There is only one duplicate number in the array, but it could be repeated more than once.


Input: [1,3,4,2,2]
Output: 2
Input: [3,1,3,4,2]
Output: 3

*/
#include<bits/stdc++.h>
using namespace std;


//function to find the duplicate number in the array
int findDuplicate(vector<int>& nums) 
{
       int n=nums.size();
        int i;
        for(i=0;i<n;i++)
        {
            if(nums[abs(nums[i])-1] < 0)
               break;
            nums[abs(nums[i])-1]*=(-1);
        }
        return abs(nums[i]);
}

//main function 
// n : size of array
// a : unsorted array of integers containing 1 to n integers only
int main()
{
    int n;
    cin>>n;
    vector<int> a;
    int x;
    for(int i=0;i<n;i++)
    {
        cin>>x;
        a.push_back(x);
    }
    findDuplicate(a);
}
