//Given an array A of integers, return true if and only if it is a valid mountain array.

//Recall that A is a mountain array if and only if:

    //A.length >= 3
  //There exists some i with 0 < i < A.length - 1 such that:
  //      A[0] < A[1] < ... A[i-1] < A[i]
  //      A[i] > A[i+1] > ... > A[A.length - 1]
  
  class Solution {
    public boolean validMountainArray(int[] A) {
      if (A.length < 3) return false;
      int start = 0;
      int end = A.length-1;
      while (start < end) {
        if (A[start+1] > A[start]) {
          start++;
        } else if (A[end-1] > A[end]) { 
          end--;
        } else {
          break;
        }
      }
      return start != 0 && end != A.length-1 && start == end;
    }
  }

