class Solution {
    public int maxArea(int[] height) {
        
        int ans=0;  
        int n=height.length;
        for(int i=0;i<n-1;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                int a=height[i];
                int b=height[j];
                
                int k=0;
                if(a>b)
                {
                    k=b*(j-i);
                }
                else
                {
                    k=a*(j-i);
                }
                
                if(ans<k)
                {
                    ans=k;
                }
                        
            }
        }
        
        return ans;
        
    }
}
