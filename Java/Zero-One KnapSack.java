import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for(int i=0;i<n;i++)
            values[i]=scn.nextInt();
            
         for(int i=0;i<n;i++)
            weights[i]=scn.nextInt();
            
        int tar = scn.nextInt();
        
        int[][] dp = new int[n+1][tar+1];
        
        for(int i=0;i<dp.length;i++){
            for(int j =0;j<=tar;j++){
                if(i==0){
                    dp[i][j]=0;
                }else if(j==0){
                    dp[i][j]=0;
                }else{
                    int val = values[i-1];
                    int wt = weights[i-1];
                    if(j<wt){
                        dp[i][j]=dp[i-1][j];
                    }else{
                        dp[i][j]=Math.max(dp[i-1][j],dp[i-1][j-wt]+val);
                    }
                }
            }
        }
        
        System.out.println(dp[n][tar]);
    }
}