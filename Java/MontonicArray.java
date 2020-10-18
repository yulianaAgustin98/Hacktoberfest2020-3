//An array is monotonic if it is either monotone increasing or monotone decreasing.

//An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

//Return true if and only if the given array A is monotonic.

class Solution {
  public boolean isMonotonic(int[] A) {
        int l = A.length;
        if (l == 1) {
            return true;
        }

        int i = 0;
        boolean isIncreasing = false;
        while (i + 1 < l) {
            if (A[i] != A[i + 1]) {
                isIncreasing = A[i + 1] > A[i];
                break;
            }
            ++i;
        }
        ++i;
        while (i + 1 < l) {
            if (A[i + 1] != A[i] && A[i + 1] > A[i] != isIncreasing) {
                return false;
            }
            ++i;
        }

        return true;
    }
}
