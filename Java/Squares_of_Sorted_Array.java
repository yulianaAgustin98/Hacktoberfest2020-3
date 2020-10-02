//Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
class Solution {
    public int[] sortedSquares(int[] A) {
        int n=A.length;
		int[]ans=new int[n];
		for(int i=0;i<n;i++) {
			ans[i]=A[i]*A[i];
        }
        Arrays.sort(ans);
   return  ans;

    }
}
