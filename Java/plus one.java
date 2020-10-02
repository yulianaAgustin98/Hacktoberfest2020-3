class Solution {
    public int[] plusOne(int[] digits) {
        int n=digits.length-1;
        int carry=1;
        for(int i=n;i>=0;i--){
            int sum=digits[i]+carry;
            digits[i]=sum%10;
            carry=sum/10;
        }
        if(carry!=0){
            int []temp=new int[digits.length+1];
             temp[0]=carry;
            for(int i=0;i<digits.length ;i++){
                temp[i+1]=digits[i];
            }
            return temp;
        }
        
       return digits;   
    }
}
