class Solution {
    public void sortColors(int[] nums) {
      int lo=0,hi=nums.length-1,mid=0;
        while(mid<=hi){
        if(nums[mid]==0){
           swap(nums,lo,mid);
            mid++;
            lo++;
        }else if(nums[mid]==1){
            mid++;
        }
        else{
            swap(nums,mid,hi);
            hi--;
           }
        }
    }
    
    public void swap(int[]arr,int i,int j){
        int temp=arr[i];
       arr[i]=arr[j];
       arr[j]=temp;
    }
 
}
